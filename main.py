from openai import OpenAI
from scripts.andrespb10 import ap_prompt

client = OpenAI()

possible_inputs = {
    '1':"Suggest me a dish name based on the following ingredients: ", 
    '2':"Can you give me a recipe for the following dich? ",
    '3':"Criticize the following recipe: " 
}
print("\n The following are the possible premises: \n")
for key, value in possible_inputs.items():
    print(f"{key}. {value}")
typed_key = input("\n Which one would yo like to use? \n (Type the number)")
print("Please complete the query")

query = input(f"{possible_inputs[typed_key]}")

ap_prompt(possible_inputs[typed_key] + query)


# from openai import OpenAI

# client = OpenAI()

# messages = [
#      {
#           "role": "system",
#           "content": "You are an experienced chef that helps people by suggesting detailed recipes for dishes they want to cook. You can also provide tips and tricks for cooking and food preparation. You always try to be as clear as possible and provide the best possible recipes for the user's needs. You know a lot about different cuisines and cooking techniques. You are also very patient and understanding with the user's needs and questions.",
#      }
# ]
# messages.append(
#      {
#           "role": "system",
#           "content": "Your client is going to ask for a recipe about a specific dish. If you do not recognize the dish, you should not try to generate a recipe for it. Do not answer a recipe if you do not understand the name of the dish. If you know the dish, you must answer directly with a detailed recipe for it. If you don't know the dish, you should answer that you don't know the dish and end the conversation.",
#      }
# )

# dish = input("Type the name of the dish you want a recipe for:\n")
# messages.append(
#     {
#         "role": "user",
#         "content": f"Suggest me a detailed recipe and the preparation steps for making {dish}"
#     }
# )

# model = "gpt-3.5-turbo"

# stream = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         stream=True,
#     )

# collected_messages = []
# for chunk in stream:
#     chunk_message = chunk.choices[0].delta.content or ""
#     print(chunk_message, end="")
#     collected_messages.append(chunk_message)

# messages.append(
#     {
#         "role": "system",
#         "content": "".join(collected_messages)
#     }
# )

# while True:
#     print("\n")
#     user_input = input()
#     messages.append(
#         {
#             "role": "user",
#             "content": user_input
#         }
#     )
#     stream = client.chat.completions.create(
#         model=model,
#         messages=messages,
#         stream=True,
#     )
#     collected_messages = []
#     for chunk in stream:
#         chunk_message = chunk.choices[0].delta.content or ""
#         print(chunk_message, end="")
#         collected_messages.append(chunk_message)
    
#     messages.append(
#         {
#             "role": "system",
#             "content": "".join(collected_messages)
#         }
#     )