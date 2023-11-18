# Tutorial on Chat completion

from openai import OpenAI
import os


# openai.api_key  = os.getenv('openai.api_key')
client = OpenAI(
    api_key = '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',  # replace with your own API key
)

completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a language translator, skilled in translate english language to any spoken language"},
    {"role": "user", "content": "what is go in spanish."}
  ]
)

print(completion.choices[0].message.content)