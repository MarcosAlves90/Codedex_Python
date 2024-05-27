from openai import OpenAI
import os

api_key = ('')
client = OpenAI(api_key=api_key)

def generate_blog(paragraph_topic):
  response = client.chat.completions.create(
    model = 'gpt-3.5-turbo',
    messages=[
        {"role": "system", "content": "You are a helpful blog assistant."},
        {"role": "user", "content": 'Write a paragraph about the following topic. ' + paragraph_topic}
    ],
    max_tokens = 400,
    temperature = 0.3
  )

  retrieve_blog = response['choices'][0]['message']['content']

  return retrieve_blog

while True:
  answer = input('Write a paragraph? Y for yes, anything else for no. ')
  if (answer == 'Y'):
    paragraph_topic = input('What should this paragraph talk about? ')
    print(generate_blog(paragraph_topic))
  else:
    break