from openai import OpenAI

client = OpenAI()

possible_chefs = {
    '1':"Colombian chef with expertise in the Pacific region's recipes.", 
    '2':"Italian chef, deeply rooted in the rich traditions of Italian cuisine.",
}

print("\n The following are the available chef profiles: \n")
for key, value in possible_chefs.items():
    print(f"{key}. {value}")

typed_key = input("\n Which one would you like to chat with? \n (Type the number)-> ")
if typed_key == '1':
    from scripts.andrespb10 import chef_prompt
elif typed_key == '2':
    from scripts.msusanrbrown import chef_prompt

possible_inputs = {
    '1':"Suggest me a dish name based on the following ingredients: ", 
    '2':"Can you give me a recipe for the following dish? ",
    '3':"Criticize the following recipe: " 
}
print("\n The following are the possible premises: \n")
for key, value in possible_inputs.items():
    print(f"{key}. {value}")
typed_key = input("\n Which one would you like to start with? \n (Type the number)-> ")
print("\n Please complete the query \n")

query = input(f"-> {possible_inputs[typed_key]}")

chef_prompt(possible_inputs[typed_key] + query)
