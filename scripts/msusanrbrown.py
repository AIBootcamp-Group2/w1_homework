from openai import OpenAI
from main import possible_inputs

client = OpenAI()

def prompt_creation(instruction: int, text: object):
    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": "YOUR CHEF Personality"},
        {"role": "user", "content": f"{possible_inputs[instruction] + text}"}
      ]
    )
    print(completion.choices[0].message)