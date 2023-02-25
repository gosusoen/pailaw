import requests

url = 'https://www.et.gr/api/DownloadFeksApi/?fek_pdf=20230100043'
response = requests.get(url)

if response.status_code == 200:
    with open('sample.pdf', 'wb') as f:
        f.write(response.content)
    print('PDF file downloaded successfully.')
else:
    print('Error:', response.status_code, response.text)

# Open the file and read it in UTF-8 encoding
with open('sample.pdf', 'r', encoding='utf-8') as f:
    text = f.read()
    print(text)