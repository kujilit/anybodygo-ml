import openai
import os

openai.api_key = os.environ.get('OPENAI_API_KEY')

client = openai.OpenAI()

response = client.chat.completions.create(
  model="gpt-4",
  messages=[],
  temperature=0,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
)