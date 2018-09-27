import csv
import urllib3
import os
import requests
import pandas as pd
import io


url='https://docs.google.com/spreadsheets/d/10cgQNGKzKVcu2dKs4zQgdthwCrwHimpI_Rst6mnulbI/export?format=csv'
email = "ben@cookcove.com"

s = requests.get(url).content
reader = pd.read_csv(io.StringIO(s.decode('utf-8')))
for index, row in pd.DataFrame(reader).iterrows():
    if email == row[0]:
        print("YEET!")