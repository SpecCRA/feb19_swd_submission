# import modules

import pandas as pd
from nba_api.stats.static import teams
from nba_api.stats.endpoints import leaguegamefinder
from nba_api.stats.endpoints import leaguegamelog

#print(teams.get_teams())

# get all teams

teams = teams.get_teams()

#print(type(teams))
#print(teams[1])

# get list of team IDs

team_ids = list() # list of all team IDs
team_abbrev = list() # list of all team abbreviations
for i in teams: # append lists team IDs and names
    team_ids.append(i['id'])
    team_abbrev.append(i['abbreviation'])

#print(team_ids)

season = '2018-19' # current season

grab_game_data = leaguegamelog.LeagueGameLog(season_all_time=season) # grab games from current season
game_data = grab_game_data.get_data_frames()[0]

#print(list(game_data)) # check column titles
#print(game_data[['TEAM_ABBREVIATION', 'GAME_DATE', 'PTS']].head(n=10))

#print(game_data.head(n=5))

# output dataframe to CSV for visualizatoin later

file_name = '2018_19_games_data.csv'
game_data.to_csv(file_name)