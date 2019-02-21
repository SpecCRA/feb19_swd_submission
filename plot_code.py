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
			hoverinfo='none',
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
			hoverinfo='none',
			line=dict(width=4, color=rockets_red) # wider than normal and red
			))
	elif team == 'Dallas Mavericks':
		traces.append(go.Scatter(
			x=data.GAME_DATE,
			y=data.PTS,
			mode='lines',
			name=team,
			hoverinfo='none',
			line=dict(width=4, color=mavs_blue) # same as rockets, but blue
			))

# Max points dot
traces.append(go.Scatter(
	x=highest_scoring_game.GAME_DATE,
	y=highest_scoring_game.PTS,
	name='San Antonio Spurs: 154 points',
	mode='markers',
	marker=dict(size=15, color='rgb(130, 130, 130)')
	))

# Min points dot
traces.append(go.Scatter(
	x=lowest_scoring_game.GAME_DATE,
	y=lowest_scoring_game.PTS,
	name='Utah Jazz: 68 points',
	mode='markers',
	marker=dict(size=15, color='rgb(130, 130, 130)')
	))

# Most 3-pointers made by a team game
# traces.append(go.Scatter(
# 	x=most_3pt_made_game.GAME_DATE,
# 	y=most_3pt_made_game.PTS,
# 	name='Houston Rockets: 26 3PM',
# 	mode='markers',
# 	marker=dict(size=15, color=rockets_red)
# 	))

# layout details
layout=go.Layout(
	xaxis=dict(
		showgrid=False,
		showticklabels=False,
		showline=False,
		linewidth=1
		),
	yaxis=dict(
		showgrid=False,
		showticklabels=True,
		tickvals=[80, 110, 140],
		showline=False,
		linecolor='rgb(204, 204, 204)',
		linewidth=1,
		ticks='outside',
		tickwidth=2,
		ticklen=5
		),
	autosize=False,
	width=1000,
	height=650,
	showlegend=False,
	margin=dict(
		autoexpand=False,
		l=100,
		r=20,
		t=200,
		b=100,
		pad=4
		)
	)

# Annotations
# Rockets have highest scoring variance. - maybe label at max points
# Mavericks are most consistent in scoring. - maybe label at max points

annotations=list()

# Title - Points scored per game by teams over time
annotations.append(dict(
	xref='paper', yref='paper', # relative point by section of plot
	x=-0.065, y=0.95,
	xanchor='left', yanchor='middle',
	text='Points',
	font=dict(family='Arial', size=16, color='rgb(0,0,0)'),
	showarrow=False
	))

# Data source - stats.nba.com, +plug nba_api!
annotations.append(dict( # annotation for stats.nba.com
	xref='paper', yref='paper',
	x=0.7, y=-0.18,
	xanchor='left', yanchor='center',
	text='Source: stats.nba.com',
	font=dict(family='Arial', size=12, color='rgb(204, 204, 204)'),
	showarrow=False
	))

annotations.append(dict(
	xref='paper', yref='paper',
	x=0.7, y=-0.22,
	xanchor='left', yanchor='center',
	text='API: https://github.com/swar/nba_api',
	font=dict(family='Arial', size=12, color='rgb(204,204,204)'),
	showarrow=False
	))

# Edited with photopea
annotations.append(dict(
	xref='paper', yref='paper',
	x=0.7, y=-0.26,
	xanchor='left', yanchor='center',
	text='Edited with: https://www.photopea.com/',
	font=dict(family='Arial', size=12, color='rgb(204,204,204)'),
	showarrow=False
	))

# Append annotations to layout
layout['annotations'] = annotations

# Finally, show plot
fig = go.Figure(data=traces, layout=layout)
py.iplot(fig, filename='pts_scored_over_time')

# The rest will be done on a picture editor.
# Color Houston Rockets and Dallas Mavericks text on the titles.