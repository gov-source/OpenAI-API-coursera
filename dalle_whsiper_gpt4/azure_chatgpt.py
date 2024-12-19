import os
from openai import AzureOpenAI
from dotenv import load_dotenv
from os.path import dirname

current_dir = dirname(os.path.abspath(__file__))
root_dir = dirname(dirname(current_dir))
env_file = os.path.join(root_dir, '.env')
load_dotenv(env_file)

# client = AzureOpenAI(azure_endpoint=os.environ["OPENAI_API_BASE"],
# api_version=os.environ["OPENAI_API_VERSION"],
# api_key=os.environ["OPENAI_API_KEY"])

client = AzureOpenAI(
    azure_endpoint=os.getenv("AZURE_ENDPOINT"),  # Changed variable name
    api_version=os.getenv("API_VERSION"),        # Changed variable name
    api_key=os.getenv("API_KEY")                 # Changed variable name
)
    
def ai_chat(user_message):
    message_text = [
        {"role": "system", "content": "You are an AI assistant that helps people find information."},
        {"role": "user", "content": user_message}
    ]

    completion = client.chat.completions.create(model="gpt-4o-mini",
    messages=message_text,
    temperature=1,
    max_tokens=800,
    top_p=0.95,
    frequency_penalty=0,
    presence_penalty=0,
    stop=None)
    return completion

print("Welcome! How can I help you today?")
while True:
    user_message = input(">>> ")
    completion = ai_chat(user_message)
    print(completion.choices[0].message.content)