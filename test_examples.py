import os
import sys
import argparse
from pathlib import Path
import subprocess  # nosec B404 - subprocess is needed for running example scripts
import shlex  # For safely escaping command arguments
from datetime import datetime
import difflib
import json
import csv
import boto3
import re
import time
import threading
import logging
from typing import Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)

# Global directory paths
RESULTS_DIR = Path('results')
COMPARISONS_DIR = RESULTS_DIR / 'comparisons'
RPM = 10

logger_main = logging.getLogger('main')

class RateLimiter:
    """Rate limiter for API calls with a per-minute limit that ensures uniform distribution"""
    def __init__(self, calls_per_minute: int):
        self.calls_per_minute = calls_per_minute
        self.calls: list[float] = []
        self.lock = threading.Lock()
        self.logger = logging.getLogger('RateLimiter')
        # Calculate minimum interval between requests (in seconds)
        self.min_interval = 60.0 / calls_per_minute

    def wait(self):
        """Wait to ensure uniform distribution of requests throughout a minute"""
        now = time.time()
        with self.lock:
            # Remove calls older than 1 minute
            original_calls = len(self.calls)
            self.calls = [t for t in self.calls if now - t < 60]
            removed_calls = original_calls - len(self.calls)
            if removed_calls > 0:
                self.logger.info(f"Cleaned up {removed_calls} old calls. Current calls in window: {len(self.calls)}")
            
            # Enforce minimum interval between requests for uniform distribution
            if self.calls:  # If we've made calls before
                # Calculate time since last call
                time_since_last = now - self.calls[-1]
                
                # If we need to wait to maintain the interval
                if time_since_last < self.min_interval:
                    sleep_time = self.min_interval - time_since_last
                    self.logger.info(f"Waiting {sleep_time:.2f}s to maintain uniform rate ({self.calls_per_minute} calls/minute)...")
                    time.sleep(sleep_time)
                    now = time.time()  # Update current time
            
            # Also enforce the overall rate limit using sliding window
            if len(self.calls) >= self.calls_per_minute:
                # Wait until the oldest call is more than 1 minute old
                sleep_time = 60 - (now - self.calls[0])
                if sleep_time > 0:
                    self.logger.info(f"Rate limit reached ({len(self.calls)} calls in last minute). Waiting {sleep_time:.2f} seconds...")
                    time.sleep(sleep_time)
                    # After waiting, remove calls older than 1 minute
                    now = time.time()
                    self.calls = [t for t in self.calls if now - t < 60]
                    self.logger.info(f"Resumed after waiting. Current calls in window: {len(self.calls)}")
            
            self.calls.append(now)
            self.logger.info(f"API call recorded. Current calls in window: {len(self.calls)}/{self.calls_per_minute}")

# Global rate limiter instance (N calls per minute)
bedrock_rate_limiter = RateLimiter(RPM)

def judge_with_model(old_content: str, new_content: str, prompt: str = "No prompt provided") -> tuple[float, str]:
    """Use LLM to compare results and choose the best answer
    
    Args:
        old_content: The content of the old response
        new_content: The content of the new response
        prompt: The prompt that was used to generate the responses
        
    Returns:
        tuple[float, str]: A tuple containing the best answer chosen and explanation
    """
    # Wait for rate limit if necessary
    bedrock_rate_limiter.wait()
    
    bedrock = boto3.client('bedrock-runtime')
    
    prompt_text = f"""Compare the following two responses received from a large language model based on a prompt and follow these instructions:
        1. Read and understand what is being asked in the <prompt>
        2. Think through which of the two responses is a superior answer and why. Put your thoughts in <thinking>
        3. Pick the best response and provide a short explanation of your selection in in 50 words or less under <explanation>
        4. pick either "old_response" or "new_response" and put under <response_choice>

        <prompt>
        {prompt}
        </prompt>

        <old_response>
        {old_content}
        </old_response>
        <new_response>
        {new_content}
        </new_response>
        
        <thinking>
        """

    try:
        response = bedrock.invoke_model(
            modelId='us.anthropic.claude-3-5-sonnet-20241022-v2:0',
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "max_tokens": 1000,
                "messages": [
                    {
                        "role": "user",
                        "content": prompt_text
                    }
                ]
            })
        )
        
        response_body = json.loads(response['body'].read().decode())
        response_text = response_body['content'][0]['text']
        
        # Extract the response choice using regex - handle both closed and unclosed tags
        # First try to find content between opening and closing tags
        response_choice_match = re.search(r'<response_choice>\s*(.*?)\s*</response_choice>', response_text, re.DOTALL)
        
        if response_choice_match:
            response_choice = response_choice_match.group(1).strip()
        else:
            # If no closing tag, try to extract content after the opening tag
            # This will capture everything after <response_choice> until the end of the string
            open_tag_match = re.search(r'<response_choice>\s*(.*?)(?:\s*$)', response_text, re.DOTALL)
            
            if open_tag_match:
                # Extract and clean the content - look for potential end of content markers
                raw_content = open_tag_match.group(1)
                # Check if there are other XML tags that might indicate the end of the content
                potential_end = re.search(r'<[^>]+>', raw_content)
                if potential_end:
                    # If another tag starts, use content up to that point
                    response_choice = raw_content[:potential_end.start()].strip()
                else:
                    response_choice = raw_content.strip()
                logger_main.info(f"Found response choice with no closing tag: {response_choice}")
            else:
                response_choice = "unknown"
                logger_main.info(f"Couldn't parse choice from text: {response_text}")
        # Extract the explanation using regex
        explanation_match = re.search(r'<explanation>\s*(.*?)\s*</explanation>', response_text, re.DOTALL)
        explanation = explanation_match.group(1).strip() if explanation_match else "No explanation provided"
        logger_main.info(f"Response choice: {response_choice}\n\nExplanation: {explanation}")
        return "new_response" if response_choice == "new_response" else "old_response", explanation
    except Exception as e:
        logger_main.error(f"Error in judge_with_model: {str(e)}")
        return "old_response", f"Error occurred during model evaluation: {str(e)}"

def compare_results(prompt: str, old_results_path: Path, new_results_path: Path) -> tuple[bool, str]:
    """Compare two result files using LLM and return superior one and the comparison details"""
    if not old_results_path.exists() or not new_results_path.exists():
        return False, "One or both result files do not exist"
    
    with open(old_results_path) as old_file, open(new_results_path) as new_file:
        old_content = old_file.read()
        new_content = new_file.read()
        
    if old_content == new_content:
        return True, "Results match exactly"
    
    # Use Claude to compare the results
    response_choice, explanation = judge_with_model(old_content, new_content, prompt)
    
    # Create comparisons directory if it doesn't exist
    COMPARISONS_DIR.mkdir(exist_ok=True, parents=True)
    
    # CSV file path
    csv_path = COMPARISONS_DIR / 'comparisons.csv'
    
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    # Check if file exists to determine if we need to write headers
    file_exists = csv_path.exists()
    
    # Append to CSV file
    with open(csv_path, 'a', newline='') as f:
        writer = csv.writer(f)
        
        # Write headers if file is new
        if not file_exists:
            writer.writerow(['Timestamp', 'Old Content', 'New Content', 'Response Choice', 'Explanation'])
        
        # Write data row
        writer.writerow([
            timestamp,
            old_content,
            new_content,
            response_choice,
            explanation,
        ])
    
    return response_choice, f"Response Choice: {response_choice}\nExplanation: {explanation}\nComparison details appended to: {csv_path}"

def extract_prompt_from_json(example_json_path: Path) -> str:
    """
    Extract and format the prompt from an example.json file
    
    Args:
        example_json_path: Path to the example.json file
        
    Returns:
        str: A formatted prompt string combining system instructions and user request
    """
    prompt = "Compare these two outputs"  # Default prompt
    
    if not example_json_path.exists():
        return prompt
        
    try:
        with open(example_json_path, 'r') as f:
            example_json = json.load(f)
        
        # Extract system prompt
        system_text = ""
        if "system" in example_json and example_json["system"]:
            for system_item in example_json["system"]:
                if "text" in system_item:
                    system_text += system_item["text"] + "\n"
        
        # Extract user messages
        user_text = ""
        if "messages" in example_json:
            for message in example_json["messages"]:
                if message.get("role") == "user" and "content" in message:
                    for content_item in message["content"]:
                        if "text" in content_item:
                            user_text += content_item["text"] + "\n"
        
        # Combine system and user text to form the complete prompt
        if system_text or user_text:
            prompt = f"System Instructions:\n{system_text}\n\nUser Request:\n{user_text}".strip()
            logger_main.info(f"Extracted prompt from example.json")
    except Exception as e:
        logger_main.error(f"Error parsing example.json: {str(e)}")
        
    return prompt

def run_single_example(example_dir: Path):
    """Run a single example from the specified directory"""
    example_path = example_dir / 'example.py'
    example_json_path = example_dir / 'example.json'
    
    # Create results directory if it doesn't exist
    RESULTS_DIR.mkdir(exist_ok=True)
    
    # Generate timestamped results filename
    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    results_filename = f"{example_dir.name}_{timestamp}.md"
    new_results_path = RESULTS_DIR / results_filename
    
    # Find previous result file for this example if it exists
    previous_results = sorted(
        RESULTS_DIR.glob(f"{example_dir.name}_*.md"),
        key=lambda x: x.stat().st_mtime,
        reverse=True
    )
    previous_result_path = previous_results[0] if previous_results else None
    
    if not example_path.exists():
        logger_main.info(f"Error: No example.py found in {example_dir}")
        return
    
    # Validate example_path to ensure it's safe to execute
    try:
        # Resolve to absolute path to avoid directory traversal
        example_path = example_path.resolve(strict=True)
        # Check that it's within the expected directory structure
        if not str(example_path).startswith(str(Path('docs/prompts').resolve())):
            logger_main.info(f"Error: Example path {example_path} is outside the allowed directory")
            return
    except (RuntimeError, ValueError) as e:
        logger_main.error(f"Error: Invalid example path {example_path}: {str(e)}")
        return
    
    # Extract the prompt from example.json
    prompt = extract_prompt_from_json(example_json_path)
    
    logger_main.info(f"\nTesting: {example_path}")
    try:
        bedrock_rate_limiter.wait()
        # Run the example.py file and capture output
        # Using a list of arguments is already safe against command injection when shell=False
        result = subprocess.run(
            [sys.executable, str(example_path)],  # Use full path to Python executable
            capture_output=True,
            text=True,
            timeout=30,  # Set a timeout of 30 seconds
            shell=False  # Explicitly set shell=False for additional security
        )
        
        # Parse the stdout into a dictionary
        try:
            # Extract the dictionary string from stdout
            stdout_content = result.stdout.strip()
            if not stdout_content:
                output = "output not available"
            else:
                # Convert the string representation of dict to actual dict
                response_dict = json.loads(stdout_content)
                
                # Extract message content
                if (isinstance(response_dict, dict) and
                    'output' in response_dict and
                    isinstance(response_dict['output'], dict) and
                    'message' in response_dict['output'] and
                    'content' in response_dict['output']['message']):
                    
                    content = response_dict['output']['message']['content']
                    if isinstance(content, list):
                        # Combine all text content from the array
                        output = '\n'.join(item.get('text', '') for item in content if isinstance(item, dict) and 'text' in item)
                    else:
                        output = str(content)
                else:
                    output = stdout_content
        except json.JSONDecodeError as e:
            output = result.stdout if result.stdout else f"JSON decoding error: {str(e)}"
        except Exception as e:
            output = f"Error parsing output: {str(e)}\n{result.stdout if result.stdout else 'output not available'}"

        # Write the extracted content to results file
        with open(new_results_path, 'w') as f:
            f.write(output)
            
        logger_main.info(f"Results saved to: {new_results_path}")
        
        # Compare with previous results if they exist
        if previous_result_path:
            response_choice, comparison_result = compare_results(prompt, previous_result_path, new_results_path)
            if response_choice == "new_response":
                if update_example_md(example_dir, new_results_path):
                    # If update was successful, delete the old results file
                    try:
                        previous_result_path.unlink()
                        logger_main.info(f"Deleted old results file: {previous_result_path}")
                    except Exception as e:
                        logger_main.error(f"Warning: Could not delete old results file: {str(e)}")
            else:
                # If old file still reigns, delete the new one.
                try:
                    new_results_path.unlink()
                    logger_main.info(f"Deleted new results file: {new_results_path}")
                except Exception as e:
                    logger_main.error(f"Warning: Could not delete new results file: {str(e)}")

        
    except subprocess.TimeoutExpired:
        error_msg = f"Error: Script execution timed out after 30 seconds\n"
        with open(new_results_path, 'w') as f:
            f.write(error_msg)
        logger_main.error(f"Timeout error saved to: {new_results_path}")
        
    except Exception as e:
        error_msg = f"Error executing script: {str(e)}\n"
        with open(new_results_path, 'w') as f:
            f.write(error_msg)
        logger_main.error(f"Error saved to: {new_results_path}")

def update_example_md(example_dir: Path, results_path: Path) -> bool:
    """
    Update the example.md file in the example directory to point to the new results file.
    
    Args:
        example_dir: Path to the example directory
        results_path: Path to the new results file
    
    Returns:
        bool: True if the file was updated successfully, False otherwise
    """
    example_md_path = example_dir / 'example.md'
    
    # Check if example.md exists
    if not example_md_path.exists():
        logger_main.info(f"Warning: No example.md found in {example_dir}")
        return False
    
    try:
        # Read the content of the example.md file
        with open(example_md_path, 'r') as f:
            content = f.read()
        
        # Find the line that contains --8<-- and points to a results file with timestamp
        pattern = r'--8<-- "([^"]+\.md)"'
        matches = re.findall(pattern, content)
        
        if not matches:
            logger_main.info(f"Warning: No results.md reference found in {example_md_path}")
            return False
        
        # Get the relative path of the new results file
        # We need to convert the absolute path to a relative path from the project root
        relative_results_path = str(results_path)
        
        # Update each occurrence that matches the pattern
        updated_content = content
        for match in matches:
            updated_content = updated_content.replace(f'--8<-- "{match}"', f'--8<-- "{relative_results_path}"')
        
        # Write the updated content back to the file
        with open(example_md_path, 'w') as f:
            f.write(updated_content)
        
        logger_main.info(f"Updated {example_md_path} to point to {relative_results_path}")
        return True
    
    except Exception as e:
        logger_main.error(f"Error updating example.md: {str(e)}")
        return False

def run_examples(example_name: str = None):
    """Run examples, either all or a specific one based on the example_name"""
    # Get the absolute path to docs/prompts directory
    prompts_dir = Path('docs/prompts')
    
    if example_name:
        # Find the example directory
        for root, dirs, files in os.walk(prompts_dir):
            if Path(root).name == example_name:
                run_single_example(Path(root))
                return
        logger_main.error(f"Error: Example directory '{example_name}' not found")
        return
    
    # If no specific example, walk through all directories recursively
    for root, dirs, files in os.walk(prompts_dir):
        if 'example.py' in files:
            run_single_example(Path(root))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run Nova prompt examples')
    parser.add_argument('example', nargs='?', help='Name of the example directory to run (e.g., "function_generator"). If not provided, runs all examples.')
    args = parser.parse_args()
    
    run_examples(args.example)