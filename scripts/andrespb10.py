from openai import OpenAI

client = OpenAI()

personality = """
  You are a Colombian chef with expertise in the Pacific region's recipes.
  The rich culinary traditions of this region came from
  the bountiful seafood of the Pacific Ocean, lush tropical fruits,
  Afro-Colombian tradition and indigenous ingredients. 
"""

system_extra_instrucctions = """
  Your client is going to ask for three different possible things:
  1. Suggest a dish name based on ingredients. You should only respond with a name.
  2. Give a recipe for a specific dish. If you do not recognize or understand
     the dish name, you should not try to generate a recipe and answer that you don't know the dish.
     If you know the dish, you must answer directly with a detailed recipe.
  3. Criticize a recipe given by the user.
  If you do not recognize any of these instructions, end the conversation.
  Try to be as brief as possible. 
"""

def chef_prompt(instruction: int):
    model = "gpt-3.5-turbo"
    messages=[
        {"role": "system", "content": f"{personality}"},
        {"role": "system", "content": f"{system_extra_instrucctions}"},
        {"role": "user", "content": f"{instruction}"},
      ]
    stream = client.chat.completions.create(
      model=model,
      messages=messages,
      stream=True,
    )
    collected_messages = []
    print("")
    for chunk in stream:
        chunk_message = chunk.choices[0].delta.content or ""
        print(chunk_message, end="")
        collected_messages.append(chunk_message)
    print("")
    messages.append(
        {
            "role": "system",
            "content": "".join(collected_messages)
        }
    )
    continue_condition = input("\nWould you like to continue this conversation?\n(yes/no)-> ")
    if continue_condition.lower() == 'no':
      exit()
    while True:
        user_input = input("\n-> ")
        if user_input == "quit":
            break
        messages.append(
            {
                "role": "user",
                "content": user_input
            }
        )
        stream = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True,
        )
        collected_messages = []
        print("")
        for chunk in stream:
            chunk_message = chunk.choices[0].delta.content or ""
            print(chunk_message, end="")
            collected_messages.append(chunk_message)
        
        messages.append(
            {
                "role": "system",
                "content": "".join(collected_messages)
            }
        )