import os
import requests
from bs4 import BeautifulSoup

os.system("clear")


url = "https://www.iban.com/currency-codes"


countries = []

request = requests.get(url)
soup = BeautifulSoup(request.text, "html.parser")

table = soup.find("table")
rows = table.find_all("tr")[1:]

for row in rows:
  items = row.find_all("td")
  name = items[0].text
  code =items[2].text
  if name and code:
    if name != "No universal currency":
      country = {
        'name':name.capitalize(),
        'code': code
      }
      countries.append(country)


def ask():
  try:
    choice = int(input("#: "))
    if choice > len(countries):
      print("Choose a number from the list.")
      ask()
    else:
      country = countries[choice]
      print(f"You chose {country['name']}\nThe currency code is {country['code']}")
  except ValueError:
    print("That wasn't a number.")
    ask()


print("Hello! Please choose select a country by number:")
for index, country in enumerate(countries):
  print(f"#{index} {country['name']}")

ask()