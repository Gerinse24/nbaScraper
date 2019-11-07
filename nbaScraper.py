#! python3
# nbaScraper.py - Scrapes current day NBA scores, and prints the info to screen.

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import sys

# Sets up options for Firefox, and begins webdriver instance.
options = Options()
options.headless = True
url = webdriver.Firefox(options=options, executable_path=r'C:\Utilities\geckodriver.exe')
url.get('https://au.global.nba.com/scores/')

element = url.find_elements(By.XPATH, "//td[@class='final-score']")
team = url.find_elements(By.XPATH, "//td[@class='team-abbrv']")
s = []
t = []
for score in element:
    s.append(score.text)

for abbr in team:
    t.append(abbr.text)

for i in range(len(t)):
    print('Team: %s - Score: %s' % (t[i], s[i]))

url.close()

ex = input('When you are done type exit.\n')    # Needed user exit prompt
if ex == 'exit':
    sys.exit()
