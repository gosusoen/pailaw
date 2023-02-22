from PyPDF2 import PdfReader
import openai

# initializations
openai.api_key = "***"

model_engine = "text-davinci-002"
temperature = 1
max_tokens = 50

reader = PdfReader('examples_folder/f2.pdf')

# text calculation
text = ''
for i in range(len(reader.pages)):
    page = reader.pages[i]
    text = page.extract_text()
    response = openai.Completion.create(
        engine=model_engine,
        prompt=text,
        max_tokens=max_tokens,
        temperature=temperature,
        n=1,
        stop=None,
        frequency_penalty=0,
        presence_penalty=0,
    )
    print(text)
# text = text.replace('\n', ' ')
# text = ' '.join(text.split())


# generated_text = response.choices[0].text.strip()

# # Print the generated text
# print("Here is your generated text:\n\n")
# print(generated_text)