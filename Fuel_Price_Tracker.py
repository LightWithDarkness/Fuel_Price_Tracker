import requests
import pandas as pd
from bs4 import BeautifulSoup

def fetch_html_content(url):
    response = requests.get(url)
    return response.text

html_content = fetch_html_content("https://www.goodreturns.in/petrol-price.html")
parsed_data = BeautifulSoup(html_content, 'html.parser')

data_string = ''
data_list = []

for row in parsed_data.find_all('tr'):
    data_string += row.get_text()

data_string = data_string[1:]
items = data_string.split("\n\n")

for entry in items[:-5]:
    data_list.append(entry.split("\n"))

df = pd.DataFrame(data_list[:-8])
df
