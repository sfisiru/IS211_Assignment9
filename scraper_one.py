
# Scraping NBA MVP winners table from Wikipedia
# URL: https://en.wikipedia.org/wiki/NBA_Most_Valuable_Player
 
import requests
from bs4 import BeautifulSoup
 
url = "https://en.wikipedia.org/wiki/NBA_Most_Valuable_Player"
 
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
 
            if len(cells) < 5:
                continue
 
            season = cells[0].text.strip()
            player = cells[1].text.strip()
            position = cells[2].text.strip()
            nationality = cells[3].text.strip()
            team = cells[4].text.strip()
 
            if season == "Season":
                continue
 
            for symbol in ["*", "^", "†"]:
                player = player.replace(symbol, "")
            player = player.strip()
 
            print(season, "-", player, "-", position, "-", nationality, "-", team)