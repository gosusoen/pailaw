import requests
from io import BytesIO
from pdfminer.high_level import extract_text
import datetime
import pytz

timezone = pytz.timezone('Europe/Athens')
current_time = datetime.datetime.now(timezone)
current_year = current_time.year

class CounterClass:
    def __init__(self):
        self.year = 2023
        self.category = 1
        self.counter = 1

obj = CounterClass()

def itteratefiles():
    calculate=True
    emptyitterations = 0
    text=""

    while calculate:
        url = f'https://www.et.gr/api/DownloadFeksApi/?fek_pdf={obj.year}{calculatestring(obj.category, 2)}{calculatestring(obj.counter, 5)}'
        response = requests.get(url)
        if response.status_code == 200:
            with BytesIO(response.content) as f:
                text = extract_text(f)
                text = text.replace("\n", " ")
                text = text.replace("- ", "")
                # print(f'success {obj.year}{calculatestring(obj.category, 2)}{calculatestring(obj.counter, 5)}\n')
                print(text)
        elif response.status_code == 500:
            print('error 500 '+ response.status_code)
            # for every N empty api calls, we change category
            emptyitterations+=1
            if(emptyitterations > 4):
                emptyitterations = 0
                increment(obj)
        else:
            print('error other '+ response.status_code)
        calculate = increment(obj)
        # print(f'{obj.year}{calculatestring(obj.category, 2)}{calculatestring(obj.counter, 5)}\n')

def increment(obj):
    result = True
    if obj.counter < 99:
            obj.counter+=1
    else:
        obj.counter=1
        if obj.category < 20:
            obj.category+=1
        else:
            obj.year+=1
            obj.category=1
            obj.counter=1          
            if obj.year > current_year:
                result = False
    return result


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