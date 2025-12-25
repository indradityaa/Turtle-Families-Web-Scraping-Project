from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://www.scrapethissite.com/pages/frames/?frame=i'

page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')

turtles = soup.find_all('div', class_=['col-md-4', 'turtle-family-card'])

data_turtle = []

for turtle in turtles :
  name = turtle.find('h3', class_='family-name').text.strip()

  data_turtle.append({
    'name' : name
  })


names = []

for item in data_turtle :
  names.append(item['name'])

outter_url = 'https://www.scrapethissite.com/pages/frames/?frame=i&family={}'

turtle_details = []

for page_full in names :
  full_url = outter_url.format(page_full)

  page_full = requests.get(full_url)
  soup = BeautifulSoup(page_full.text, 'html.parser')

  details = soup.find_all('div', class_=['col-md-6', 'col-md-offset-3', 'turtle-family-detail'])

  for detail in details :
    name = detail.find('h3', class_='family-name').text.strip()
    description = detail.find('p', class_='lead').text.strip()

    turtle_details.append({
      'name' : name,
      'description' : description
    })


df = pd.DataFrame(turtle_details)
df.to_csv('data/turtle_details.csv', index=False)

print('Data saved to data/turtle_details.csv')