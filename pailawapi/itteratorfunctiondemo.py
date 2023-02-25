import requests
from io import BytesIO
from pdfminer.high_level import extract_text

url = 'https://www.et.gr/api/DownloadFeksApi/?fek_pdf=20230100043'
response = requests.get(url)

if response.status_code == 200:
    with BytesIO(response.content) as f:
        text = extract_text(f)
    print('PDF file downloaded and text extracted successfully.')
else:
    print('Error:', response.status_code, response.text)

print(text)