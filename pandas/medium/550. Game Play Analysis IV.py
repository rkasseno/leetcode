# to solve
import pandas as pd

activity = pd.DataFrame({
    'player_id': [1, 1, 3, 3],
    'device_id': [2, 2, 1, 4],
    'event_date': ['2016-03-01', '2016-03-02', '2016-01-02', '2016-01-03'],
    'games_played': [5, 1, 10, 15]
})

if len(activity) == 1:
    
    print(pd.DataFrame({'fraction' : [None]}))

total_players = len(activity.player_id.unique())
activity.sort_values(by='player_id', inplace=True)
logged_players = {}
activity.event_date = pd.to_datetime(activity.event_date, errors='coerce')

for i in range(1, len(activity.player_id)):
    if activity.player_id[i] == activity.player_id[i-1]:
        if (activity.event_date[i] - activity.event_date[i-1]).days == 1:
            logged_players[activity.player_id[i]] = True

fraction = pd.DataFrame({'fraction' : [(len(logged_players.keys()) / total_players + 0.555555)]})

print(fraction)
