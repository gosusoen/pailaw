import openai

# Set up the OpenAI API client with your API key
openai.api_key = "***"

# Define the GPT-3 model and parameters
model_engine = "text-davinci-002"  # replace with the name of your fine-tuned model
temperature = 0.8
max_tokens = 50

# Define the question you want to ask the model
question = "Ποιός είναι ο σκοπός της Συμφωνίας?"

# Generate a response from the model
response = openai.Completion.create(
    engine=model_engine,
    prompt=question,
    max_tokens=max_tokens,
    temperature=temperature,
)

# Print the response text
print("Here is the model's response:\n\n")
print(response.choices[0].text.strip())