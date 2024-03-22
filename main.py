from openai import OpenAI

client = OpenAI()

possible_inputs = {
    '1':"Suggest me a dish based on the following ingredients ", 
    '2':"Can you give me a recipe for the following dich? ",
    '3':"Criticize the following recipe " 
}
print("\n The following are the possible premises: \n")
for key, value in possible_inputs.items():
    print(f"{key}. {value}")
typed_key = input("\n Which one would yo like to use? \n (Type the number)")
print(f"\n You selected: \n {possible_inputs[typed_key]}")
