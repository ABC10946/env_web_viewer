import time
import requests
import pandas as pd
from pandas.io.json import json_normalize

url = 'http://192.168.3.51:5000'
csv_file_path = '../data/environ.csv'

while True:
    r = requests.get(url)
    if 'json' in r.headers.get('content-type'):
        rec_json = r.json()
        timestamp = rec_json['timestamp']
        temp = rec_json['temp']
        press = rec_json['press']
        humid = rec_json['humid']
        with open(csv_file_path, 'a') as f:
            f.write(str(timestamp) + ',' + str(temp) + ',' +
                    str(press) + ',' + str(humid) + '\n')

        print("Process complete")
        time.sleep(600)

    else:
        print("Response is not json Error")
        time.sleep(5)
