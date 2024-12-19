import os
import openai

openai.api_type = "azure"
openai.api_base = "https://coursera-azure-openai-service.openai.azure.com/"
openai.api_version = "2024-02-15-preview"
openai.api_key = "D68tqjlf1v9kwYmcLyRfzIbbSErkJHBPNinuew6m1HZafg5pOksGJQQJ99ALACYeBjFXJ3w3AAABACOGeUCa"

def ai_chat(user_message):
    message_text = [
        {"role": "system", "content": "You are an AI assistant that helps people find information."},
        {"role": "user", "content": user_message}
    ]
    
    completion = openai.ChatCompletion.create(
        engine="gpt-4o-mini",
        messages=message_text,
        temperature=1,
        max_tokens=800,
        top_p=0.95,
        frequency_penalty=0,
        presence_penalty=0,
        stop=None
    )
    return completion

print("Welcome! How can I help you today?")
while True:
    user_message = input(">>> ")
    completion = ai_chat(user_message)
    print(completion['choices'][0]['message']['content'])