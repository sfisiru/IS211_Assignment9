# Scraping World Series Records by franchise table from Wikipedia
# URL: https://en.wikipedia.org/wiki/List_of_World_Series_champions
 
import requests
from bs4 import BeautifulSoup
 
url = "https://en.wikipedia.org/wiki/List_of_World_Series_champions"
 
headers = {"User-Agent": "Mozilla/5.0"}
response = requests.get(url, headers=headers)
 
if response.status_code != 200:
    print("Failed to load page. Status code:", response.status_code)
else:
    soup = BeautifulSoup(response.text, "html.parser")
 
    tables = soup.find_all("table", class_="wikitable")
    table = tables[1]
 
    if not table:
        print("Could not find the table on the page.")
    else:
        rows = table.find_all("tr")
 
        for row in rows:
            cells = row.find_all(["th", "td"])
 
            if len(cells) < 4:
                continue
 
            year = cells[0].text.strip()
            winning_team = cells[1].text.strip()
            series = cells[3].text.strip()
            losing_team = cells[4].text.strip()
 
            if year == "Year":
                continue
 
            print(year, "-", winning_team, "-", series, "-", losing_team)