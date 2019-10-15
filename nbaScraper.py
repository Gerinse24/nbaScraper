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
for tag in soup.find_all("td", {"class":"final-score"}):    # Finds all scores from todays games and stores them in total.
    total.append(tag.text)

for team in soup.find_all("td", {"class":"team-abbrv"}):    # Finds team abbreviations from todays games and stores them in teams.
    teams.append(team.text)

for i in range(len(total)):     # Iterates over the len of total which will be the same as the amount of teams, and prints them.
    print(teams[i] + ' ' + total[i])
