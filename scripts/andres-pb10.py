from openai import OpenAI
from main import possible_inputs

client = OpenAI()

personality = """
  You are a Colombian chef with expertise in the Pacific region's recipes.
  The rich culinary traditions of this region came from
  the bountiful seafood of the Pacific Ocean, lush tropical fruits,
  Afro-Colombian tradition and indigenous ingredients. 
"""
def prompt_creation(instruction: int, text: object):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": f"{personality}"},
        {"role": "user", "content": f"{possible_inputs[instruction] + text}"}
      ]
    )
    print(completion.choices[0].message)