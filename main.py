from openai import OpenAI
from scripts.andrespb10 import ap_prompt

client = OpenAI()

possible_inputs = {
    '1':"Suggest me a dish name based on the following ingredients: ", 
    '2':"Can you give me a recipe for the following dish? ",
    '3':"Criticize the following recipe: " 
}
print("\n The following are the possible premises: \n")
for key, value in possible_inputs.items():
    print(f"{key}. {value}")
typed_key = input("\n Which one would yo like to start with? \n (Type the number)")
print("\n Please complete the query \n")

query = input(f"{possible_inputs[typed_key]}")

ap_prompt(possible_inputs[typed_key] + query)
