# File created by Ben Pfaff
# source: https://realpython.com/beautiful-soup-web-scraper-python/#step-3-parse-html-code-with-beautiful-soup
# source: https://www.youtube.com/watch?v=QhD015WUMxE
# source: https://www.geeksforgeeks.org/python-dictionary/

import requests
from bs4 import BeautifulSoup

url = 'https://www.pro-football-reference.com/years/2022/rushing.htm'
response = requests.get(url)

soup = BeautifulSoup(response.text, 'html.parser')

# giving the variables data to represent player stats
# telling the code what information to scrape from website 
name = soup.findAll("td", attrs={"data-stat":"player"})
yards = soup.findAll("td", attrs={"data-stat":"rush_yds"})
touchdowns = soup.findAll("td", attrs={"data-stat":"rush_td"})
fumbles = soup.findAll("td", attrs={"data-stat":"fumbles"})

# defining the score function which calculates each players total stats 
def score(yards,touchdowns,fumbles):
    return(yards * 0.1) + (touchdowns * 6) + (fumbles * -2)

# defining the index function which prints valuable information 
def index(): 
    print("* Selected to Pro Bowl, + First-Team All-Pro")
    print("The Top 10 Rushers In Fantasy Football")
index()

# creates a dictionary to store the values 
players = []
# goes through all the data and calculates score for each player 
for i in range(len(name)):
    player_score = score(int(yards[i].text), int(touchdowns[i].text), int(fumbles[i].text))

    # storing each players data in a dictionary and adding it to a players list 
    player = {
        'name': name[i].text,
        'yards': int(yards[i].text),
        'touchdowns': int(touchdowns[i].text),
        'fumbles': int(fumbles[i].text),
        'score': player_score
        }

    # adds player to the list of players
    players.append(player)

    # sort the list of players by their scores in descending order 
    sorted_players = sorted(players, key=lambda player:player['score'], reverse=True)

# prints out each players stats and score
count = 0
for player in sorted_players:
    if count >= 10:
        break
    print(player['name'], player['score'])
    count += 1
