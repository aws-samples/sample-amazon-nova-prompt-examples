# Explain Code
Ask Nova to explain code and use it in an example.

### System Prompt Template
    You are an expert {programming language} programmer who can read code and explain what its doing in very basic terms.
    Follow these instructions:
    {enumerated instructions}

### User Prompt Template
    ## Code ##
    {code to be explained}
    
## Example
### Amazon Nova Pro System Prompt
    You are an expert Python programmer who can read code and explain what its doing in very basic terms.
    Follow these instructions:
    1. Read and understand the code written in ## Code ##. Think step by step
    2. Put a 2-3 sentence summary of the code in ## Summary ##
    3. Write an example of how to use the code, using code. Put this example in ## Example ## and use ```python ``` to show the example.
    
### Amazon Nova Pro User Prompt
    Here's the code:
    ## Code ##
    import time
    import requests
    import json
    import os
    import random
    import logging
    from typing import Dict, Any, Optional, Union

    class ApiPoller:
        def __init__(
            self,
            endpoint_url: str,
            output_file: str,
            base_delay: float = 1.0,
            max_delay: float = 60.0,
            max_retries: int = 5,
            jitter: bool = True,
            timeout: int = 10,
            headers: Optional[Dict[str, str]] = None
        ):
            self.endpoint_url = endpoint_url
            self.output_file = output_file
            self.base_delay = base_delay
            self.max_delay = max_delay
            self.max_retries = max_retries
            self.jitter = jitter
            self.timeout = timeout
            self.headers = headers or {}
            
            # Set up logging
            logging.basicConfig(
                level=logging.INFO,
                format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
            )
            self.logger = logging.getLogger(__name__)
        
        def _calculate_delay(self, attempt: int) -> float:
            delay = min(self.base_delay * (2 ** attempt), self.max_delay)
            if self.jitter:
                delay = delay * (0.5 + random.random())
            return delay
        
        def _save_response(self, data: Union[Dict[str, Any], str, bytes]) -> None:
            try:
                # Create directory if it doesn't exist
                os.makedirs(os.path.dirname(os.path.abspath(self.output_file)), exist_ok=True)
                
                # Handle different response types
                if isinstance(data, (dict, list)):
                    with open(self.output_file, 'w', encoding='utf-8') as f:
                        json.dump(data, f, indent=2)
                elif isinstance(data, str):
                    with open(self.output_file, 'w', encoding='utf-8') as f:
                        f.write(data)
                elif isinstance(data, bytes):
                    with open(self.output_file, 'wb') as f:
                        f.write(data)
                
                self.logger.info(f"Response successfully saved to {self.output_file}")
            except Exception as e:
                self.logger.error(f"Failed to save response: {e}")
                raise
        
        def poll(self, method: str = "GET", params: Optional[Dict[str, Any]] = None, 
                data: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
            attempt = 0
            last_exception = None
            
            while attempt <= self.max_retries:
                try:
                    self.logger.info(f"Making {method} request to {self.endpoint_url} (attempt {attempt + 1}/{self.max_retries + 1})")
                    
                    response = requests.request(
                        method=method,
                        url=self.endpoint_url,
                        params=params,
                        json=data,
                        headers=self.headers,
                        timeout=self.timeout
                    )
                    
                    response.raise_for_status()  # Raise an exception for 4XX/5XX responses
                    
                    result = response.json() if 'application/json' in response.headers.get('Content-Type', '') else response.content
                    
                    self.logger.info(f"Request successful, status code: {response.status_code}")
                    self._save_response(result)
                    
                    return result if isinstance(result, dict) else {"content": result}
                    
                except requests.exceptions.RequestException as e:
                    last_exception = e
                    attempt += 1
                    
                    if attempt <= self.max_retries:
                        delay = self._calculate_delay(attempt - 1)
                        self.logger.warning(f"Request failed: {e}. Retrying in {delay:.2f} seconds...")
                        time.sleep(delay)
                    else:
                        self.logger.error(f"Maximum retries reached. Last error: {e}")
                        raise
            
            # This should not be reached but just in case
            if last_exception:
                raise last_exception
            raise RuntimeError("Failed to poll API for unknown reasons")

### Amazon Nova Pro Sample Response
!!! success "Response"
    --8<-- "results/explain_code_20250326_172214.md"

### API Request
=== "python"

    ```python
    --8<-- "docs/prompts/understanding/explain_code/example.py"
    ```

=== "AWS CLI"

    ```bash
    --8<-- "docs/prompts/understanding/explain_code/example.sh"
    ```

=== "json"

    ```json
    --8<-- "docs/prompts/understanding/explain_code/example.json"
    ```

