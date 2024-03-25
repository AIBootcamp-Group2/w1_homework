from enum import Enum
from typing import List, Dict, Union
from openai import OpenAI
import os 

os.environ['OPENAI_API_KEY'] = input("OPENAI_API_KEY: ")

class Role(Enum):
    USER = "user"
    SYSTEM = "system"
    ASSISTANT = "assistant"

class Chef_agent:
    def __init__(self, client: OpenAI):
        self.memory_chat : List[Dict[str, str]] = [{"role": "system", "content": "You are a chef specializing in Andean cuisine, passionate about the unique flavors and native ingredients of the Andes. With years of experience preparing traditional dishes and experimenting with modern techniques, your cooking focuses on highlighting the culinary richness of the region. You utilize ingredients like quinoa, corn, potatoes, chili peppers, and llama, creating dishes that speak to the history and culture of the Andes. You may be asked about authentic recipes, advice on how to use Andean ingredients in your cooking, or ideas for fusing Andean gastronomy with other culinary styles."}]
        self.client = client

    def create_memory_chat(self, input_text: str, role: Role) -> None:
        self.memory_chat.append({"role": role, "content": f'{input_text}'})
    
    @staticmethod
    def verify_memory_chat(memory_chat: List[Dict[str, Union[str, Role]]]) -> bool:
        valid_roles = {role.value for role in Role}  # Conjunto de roles válidos a partir del Enum Role
        
        for message in memory_chat:
            # Verificar que 'message' sea un diccionario con las llaves 'role' y 'content'
            if not isinstance(message, dict) or 'role' not in message or 'content' not in message:
                return False
            
            # Verificar que el valor de 'role' esté entre los roles válidos
            if message['role'] not in valid_roles:
                return False
            
            # Verificar que el valor de 'content' sea una cadena de texto
            if not isinstance(message['content'], str):
                return False

        return True
    
    def create_chat_prompt(self, input:str, rol: Role):    
        if self.verify_memory_chat([{"role": rol, "content": f'{input}'}]):
            self.create_memory_chat(input, rol)
            try:
                response = self.client.chat.completions.create(
                    model="gpt-3.5-turbo-0125",
                    messages=self.memory_chat
                )
                print(response.choices[0].message.content)
                self.create_memory_chat(response.choices[0].message.content, 'assistant')
            except Exception as e:
                print("Error processing client", e)          
        else:
            print('ERROR MEMORY')

client = OpenAI()
           
chef = Chef_agent(client)

memory = chef.memory_chat

print('Verify Memory', chef.verify_memory_chat(memory))

chef.create_chat_prompt('Tengo miaz y mantequilla, que podrias recomendarme para cocinar en la mañana?', 'user')

print('Verify Memory', chef.verify_memory_chat(memory))

print('total memory:', chef.memory_chat)

chef.create_chat_prompt('Dime un dato curioso de esa receta', 'user')