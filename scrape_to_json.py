import json
import requests
from BeautifulSoup import BeautifulSoup

url = 'http://www.showmeboone.com/sheriff/JailResidents/JailResidents.asp'
response = requests.get(url)
html = response.content
soup = BeautifulSoup(html)

table = soup.find('table', attrs={'class': 'resultsTable'})

list_of_rows = []
for row in table.findAll('tr')[1:]:
  list_of_cells = []
  for cell in row.findAll('td'):
    text = cell.text.replace('&nbsp;', '')
    list_of_cells.append(text)
  list_of_rows.append(list_of_cells)    

inmates = []
for row in list_of_rows:
  inmate = {
    "last": row[0],
    "first": row[1],
    "middle": row[2],
    "gender": row[3],
    "race": row[4],
    "age": row[5],
    "city": row[6],
    "state": row[7]
  }
  inmates.append(inmate)

file = open("./inmates.json", "wb")
output = inmates
json.dump(output, file, indent=2)
file.close()
