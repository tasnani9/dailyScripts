import openai

# Set your OpenAI API key here
api_key = ''
openai.api_key = api_key

def send_message(prompt):
    response = openai.Completion.create(
        model="davinci-002",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

if __name__ == "__main__":
    prompt = input("You: ")
    response = send_message(prompt)
    print("GPT-3.5:", response)
