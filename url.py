import csv
import urllib
import os
import requests

email = input()

url='https://docs.google.com/spreadsheets/d/10cgQNGKzKVcu2dKs4zQgdthwCrwHimpI_Rst6mnulbI/export?format=csv'
r = requests.get(url)
text = r.iter_lines()
reader = csv.reader(text, delimiter=',')
print(reader.content)