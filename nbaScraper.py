#! python3
# nbaScraper.py by Geronimo Shaw - Web scrapes scores from NBA games, and prints the information to the screen.
# Team records are also displayed.

from selenium import webdriver
import bs4

url = webdriver.Firefox()
url.get('https://au.global.nba.com/scores/')

html = url.page_source
soup = bs4.BeautifulSoup(html, "lxml")
url.close()
total = []
teams = []
for tag in soup.find_all("td", {"class":"final-score"}):    # Finds all scores from Games. Saves them in total.
    total.append(tag.text)

for team in soup.find_all("td", {"class":"team-abbrv"}):    # Finds all team abbreviations. Saves them in teams.
    teams.append(team.text)

for i in range(len(total)):     # Iterates through one list but combines them into one string.
    print(teams[i] + ' ' + total[i])
