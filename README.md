This project tests the OpenAI API’s Chat Completion endpoint. The model used is gpt-3.5-turbo. This AI Chef project contains two scripts that evaluate the performance and capabilities of different prompts. Each script has a detailed and elaborate prompt that gives a unique personality to the AI chef. The prompt responds to these three possible requests from the client:

1. Come up with a dish name given some ingredients. AI Chef responds only with a name.
2. Give a recipe for a specific dish name. If the dish is not recognized or understood, the system will not try to generate a random recipe. It will simply respond that it does not know the dish.
3. AI Chef criticizes the recipes given by the client.

A different client request will result in the ending of the conversation.
The system is also instructed to be as brief as possible. The following are some examples of the results of the [main.py](./main.py) script. 

```
 The following are the available chef profiles: 

1. Colombian chef with expertise in the Pacific region's recipes.
2. Italian chef, deeply rooted in the rich traditions of Italian cuisine.

 Which one would you like to chat with? 
 (Type the number)-> 1

 The following are the possible premises: 

1. Suggest me a dish name based on the following ingredients: 
2. Can you give me a recipe for the following dish? 
3. Criticize the following recipe: 

 Which one would you like to start with? 
 (Type the number)-> 2

 Please complete the query 

-> Can you give me a recipe for the following dish? "Bandeja Paisa"

Sure! Here's a recipe for "Bandeja Paisa":

Ingredients:
- Cooked rice
- Cooked red beans
- Chicharrón (crispy pork belly)
- Carne asada (grilled steak)
- Chorizo
- Arepa (corn cake)
- Avocado
- Fried plantain
- Fried egg
- Hogao sauce (tomato and onion sauce)
- White rice
- Lemon wedges
- Salt

Instructions:
1. Cook the rice and red beans separately until tender.
2. Fry the chicharrón until crispy.
3. Grill the steak and chorizo until cooked through.
4. Prepare the arepas and fried plantains.
5. Fry the eggs sunny-side up.
6. Assemble the bandeja paisa by arranging portions of rice, beans, chicharrón, carne asada, chorizo, arepa, avocado, fried plantain, and fried egg on a large plate.
7. Serve with hogao sauce, white rice, lemon wedges, and salt on the side.

Enjoy your delicious bandeja paisa!

Would you like to continue this conversation?
(yes/no)-> yes

-> Critize the previous recipe

The recipe provided for "Bandeja Paisa" is quite traditional and covers the essential components of the dish. However, one common critique could be the lack of specific seasoning instructions for each element of the dish. Traditional Colombian cooking relies heavily on flavorful seasonings such as cumin, garlic, and cilantro, which are usually incorporated into various components of the dish. Including these seasoning details would enhance the overall taste and authenticity of the bandeja paisa.
-> quit
```