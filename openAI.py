from openai import OpenAI
client = OpenAI()

client.completions.create(
  model="davinci-002",
  prompt="Say this is a test",
  max_tokens=7,
  temperature=0
)