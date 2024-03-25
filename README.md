This project tests the OpenAI API’s Chat Completion endpoint. The model used is gpt-3.5-turbo. This AI Chef project contains 2 scripts that evaluate the performance and capabilities of different prompts. Each script has a detailed and elaborate prompt that gives a unique personality to the AI chef. The prompt responds to this three possible requests from the client:

Give a recipe for a dish given some ingredients. AI Chef suggests a dish responding only with a name. 
Give a recipe for a specific dish name. If the dish is not recognized or understood, the system will not try to generate a random recipe. It will simply respond that it does not know the dish.

AI Chef criticizes the recipes given by the client.

A different client request will result in ending the conversation.
The system is also instructed to be as brief as possible.