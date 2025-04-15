import boto3
import json

bedrock_runtime = boto3.client(
            service_name="bedrock-runtime",
            region_name="us-west-2"
        )


response = bedrock_runtime.converse(
                modelId='us.amazon.nova-pro-v1:0',
                system=[{"text": "You are an experienced executive assistant skilled in meeting note analysis and summarization. Your primary responsibilities include distilling complex discussions into clear, actionable summaries. Follow these instructions: ##INSTRUCTIONS## 1. Read understand the meeting notes found in ##NOTES## 2. Put all of your outputs in a section called ##OUTPUTS## in markdown formatting 3. Summarize the meeting notes in 5 sentences or less. Put this in a section called \"Overall Summary\". 4. Numerically list any action items for specific people and what needs to be completed. Put this list in a section called \"Action Items\". 5. If applicable, list the topics that need to be discussed more fully in the next meeting. Put this in a section called \"Topics for Next Meeting\"."}],
                messages = [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": "##NOTES## Meeting Date: March 5th, 2050 Meeting Time: 2:00 PM Location: Conference Room 3B, Intergalactic Headquarters Attendees: - Captain Stardust - Dr. Quasar - Lady Nebula - Sir Supernova - Ms. Comet Meeting called to order by Captain Stardust at 2:05 PM 1. Introductions and welcome to our newest team member, Ms. Comet 2. Discussion of our recent mission to Planet Zog - Captain Stardust: \"Overall, a success, but communication with the Zogians was difficult. We need to improve our language skills.\" - Dr. Quasar: \"Agreed. I'll start working on a Zogian-English dictionary right away.\" - Lady Nebula: \"The Zogian food was out of this world, literally! We should consider having a Zogian food night on the ship.\" 3. Addressing the space pirate issue in Sector 7 - Sir Supernova: \"We need a better strategy for dealing with these pirates. They've already plundered three cargo ships this month.\" - Captain Stardust: \"I'll speak with Admiral Starbeam about increasing patrols in that area.\" - Dr. Quasar: \"I've been working on a new cloaking technology that could help our ships avoid detection by the pirates. I'll need a few more weeks to finalize the prototype.\" 4. Review of the annual Intergalactic Bake-Off - Lady Nebula: \"I'm happy to report that our team placed second in the competition! Our Martian Mud Pie was a big hit!\" - Ms. Comet: \"Let's aim for first place next year. I have a secret recipe for Jupiter Jello that I think could be a winner.\" 5. Planning for the upcoming charity fundraiser - Captain Stardust: \"We need some creative ideas for our booth at the Intergalactic Charity Bazaar.\" - Sir Supernova: \"How about a 'Dunk the Alien' game? We can have people throw water balloons at a volunteer dressed as an alien.\" - Dr. Quasar: \"I can set up a 'Name That Star' trivia game with prizes for the winners.\" - Lady Nebula: \"Great ideas, everyone. Let's start gathering the supplies and preparing the games.\" 6. Upcoming team-building retreat - Ms. Comet: \"I would like to propose a team-building retreat to the Moon Resort and Spa. It's a great opportunity to bond and relax after our recent missions.\" - Captain Stardust: \"Sounds like a fantastic idea. I'll check the budget and see if we can make it happen.\" 7. Next meeting agenda items - Update on the Zogian-English dictionary (Dr. Quasar) - Progress report on the cloaking technology (Dr. Quasar) - Results of increased patrols in Sector 7 (Captain Stardust) - Final preparations for the Intergalactic Charity Bazaar (All) Meeting adjourned at 3:15 PM. Next meeting scheduled for March 19th, 2050 at 2:00 PM in Conference Room 3B, Intergalactic Headquarters. ##OUTPUTS##"
                        }
                    ]
                }
            ],
            inferenceConfig={
                "temperature": 0.2,
                "topP": .9,
                "maxTokens": 2048
            }
            )


print(json.dumps(response, indent=2))