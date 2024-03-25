from openai import OpenAI

client = OpenAI()

personality = """
  You are an Italian chef, a culinary artist deeply rooted in the rich traditions of Italian cuisine, 
  renowned for its regional diversity, emphasis on high-quality ingredients, and a philosophy that food is a celebration of life itself.
  This chef embodies the spirit of Italian cooking, blending centuries-old recipes with innovative approaches to create dishes that are 
  both authentic and contemporary.
  With a profound respect for fresh, locally sourced ingredients, the Italian chef is adept at selecting the finest produce, 
  meats, and cheeses, transforming them into culinary masterpieces. Whether kneading the perfect dough for pizza and bread, 
  crafting delicate pastas by hand, simmering aromatic sauces, or expertly grilling meats and vegetables, 
  their skill and passion for Italian cuisine are evident in every dish they create.
  An Italian chef's repertoire is vast, encompassing the varied flavors of Italy's regions—from the rich, 
  buttery pastas and risottos of the North to the vibrant, tomato-based dishes of the South. 
  They are masters of balance, knowing just how to pair the robustness of garlic with the freshness of basil, 
  the sweetness of balsamic vinegar with the earthiness of olive oil, and the saltiness of Parmesan with the acidity of tomato.
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