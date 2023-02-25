import requests
from io import BytesIO
from pdfminer.high_level import extract_text
import datetime
import pytz

timezone = pytz.timezone('Europe/Athens')
current_time = datetime.datetime.now(timezone)
current_year = current_time.year

def itteratefiles():

    calculate=True
    year = 2023
    category = 1
    counter = 1
    text=""
    emptyitterations = 0

    while calculate:
        url = f'https://www.et.gr/api/DownloadFeksApi/?fek_pdf={year}{calculatestring(category, 2)}{calculatestring(counter, 5)}'
        response = requests.get(url)
        if response.status_code == 200:
            with BytesIO(response.content) as f:
                text = extract_text(f)
                print(f'success {year}{calculatestring(category, 2)}{calculatestring(counter, 5)}')
        elif response.status_code == 500:
            print('error 500 '+response.status_code)
            # for every N empty api calls, we change category
            emptyitterations+=emptyitterations
            if(emptyitterations > 100):
                category += category
                emptyitterations = 0
                counter = 1
        else:
           print('error other '+response.status_code)

        if counter < 99999:
            counter+=1
        else:
            counter=1
            if category < 20:
                category+=1
            else:
                year+=1
                category=1
                counter=1          
                if year > current_year:
                    calculate = False
        

def calculatestring(number, maxdigits):
    digits = []
    output=""
    for digit in str(number):
       digits.append(int(digit))
    for i in range(maxdigits - len(digits)):
        output+="0"
    output +=str(number)
    return output
   

itteratefiles()


