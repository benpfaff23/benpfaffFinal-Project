# File created by Ben Pfaff
# source: https://realpython.com/beautiful-soup-web-scraper-python/#step-3-parse-html-code-with-beautiful-soup
# source: https://www.youtube.com/watch?v=QhD015WUMxE

import requests
from bs4 import BeautifulSoup

url = 'https://www.pro-football-reference.com/years/2022/rushing.htm'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# giving the variables data to represent player stats
# telling the code what information to scrape from website 
name = soup.findAll("td", attrs={"data-stat":"player"})
attempts = soup.findAll("td", attrs={"data-stat":"rush_att"})
yards = soup.findAll("td", attrs={"data-stat":"rush_yds"})
touchdowns = soup.findAll("td", attrs={"data-stat":"rush_td"})
ydsperatt = soup.findAll("td", attrs={"data-stat":"rush_yds_per_att"})

# defining the index function which prints valuable information 
def index(): 
    print("* Selected to Pro Bowl, + First-Team All-Pro")

index()
# for loop that will initiate the printing of the data from the website 
for i in range(len(name)):
    print(name[i].text + ": " + attempts[i].text + " Attempts, " + yards[i].text + " Rushing Yards, " + touchdowns[i].text 
          + " Rushing Touchdowns, " + ydsperatt[i].text + " Yards Per Attempt")
    