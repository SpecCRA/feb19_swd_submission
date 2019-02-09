# Plotly code for February submission

"""
1. Plot all teams besides the Mavs and Rockets in light grey
2. Create a separate plot for the Mavs and Rockets outside of the loop
3. Annotations: label min and max points - make dots for each
"""

# assign variables for notable points
highest_scoring_game = df[df['PTS'] == 154] # single row dataframe for highest scoring game
lowest_scoring_game = df[df['PTS'] == 68] # same for lowest scoring
most_3pt_made_game = df[df.FG3M == 26] # same for most 3s made, 26

# Data for charts
traces = []

# colors data: https://teamcolorcodes.com/houston-rockets-color-codes/
mavs_blue = 'rgb((0,83,188)'
rockets_red = 'rgb((206,17,65)'

# Loop through teams to append lines
for team in teams:
	data = df[df.TEAM_NAME == team]
	if (team != 'Houston Rockets') and (team != 'Dallas Mavericks'): # draw every line besides the two teams
		traces.append(go.Scatter(
			x=data.GAME_DATE, # x-axis is the date
			y=data.PTS, # y-axis is point values
			mode='lines', # line plot
			name=team,
			line = dict(width=3, color='rgb(130, 130, 130') # thin, light grey lines per line
			))
	else:
		continue

for team in teams: # loop through again to get rockets and mavs
	data = df[df.TEAM_NAME == team]
	if team == 'Houston Rockets': 
		traces.append(go.Scatter(
			x=data.GAME_DATE,
			y=data.PTS,
			mode='lines',
			name=team,
			line=dict(width=6, color=rockets_red) # wider than normal and red
			))
	elif team == 'Dallas Mavericks':
		traces.append(go.Scatter(
			x=data.GAME_DATE,
			y=data.PTS,
			mode='lines',
			name=team,
			line=dict(width=6, color=mavs_blue) # same as rockets, but blue
			))

# Max points dot
traces.append(go.Scatter(
	x=highest_scoring_game.GAME_DATE,
	y=highest_scoring_game.PTS,
	mode='markers',
	marker=dict(size=10, color='rgb(130, 130, 130)')
	))

# Min points dot
traces.append(go.Scatter(
	x=lowest_scoring_game.GAME_DATE,
	y=lowest_scoring_game.PTS,
	mode='markers',
	marker=dict(size=10, color='rgb(130, 130, 130)')
	))

# Most 3-pointers made by a team game
traces.append(go.Scatter(
	x=most_3pt_made_game.GAME_DATE,
	y=most_3pt_made_game.PTS,
	mode='markers',
	marker=dict(size=10, color=rockets_red)
	))

# layout details
"""
1. Raise default height
2. Remove legend
3. Give it some margin space for labeling
4. Only have 2 large ticks for the y-axis
5. Remove grid lines
6. Remove x-axis lableing
"""
layout=go.Layout(
	xaxis=dict(
		),
	yaxis=dict(
		),
	autosize=False,
	showlegend=False,
	margin=dict(
		)
	)

# Annotations
annotations=list()

# Annotate max points point - 154 points by Spurs

# Annotate min points point - 68 points by Jazz
 
# Annotate game with most 3s made - 26 made by Rockets

# Label each line with a little message
# Rockets have highest scoring variance. - maybe label at max points
# Mavericks are most consistent in scoring. - maybe label at max points

# Title - 

# Data source - plug nba_api!

# 

# Finally, show plot
fig = go.Figure(data=traces)
py.iplot(fig, filename='pts_scored_over_time')