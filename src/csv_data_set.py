import pandas as pd

# read in data
df = pd.read_csv('data/nba_2020_per_game_stats_basketball_reference.csv')

# drop unnecessary data
del df['Age'], df['GS'], df['3PA'], df['3P%'], df['2P'], df['2PA']
del df['2P%'], df['eFG%'], df['ORB'], df['DRB'], df['PF']

# clean player names column
for ind in df.index:
    player_name = df['Player'][ind].split('\\')[0]
    # df['Player'][ind] = player_name
    df.loc[ind, ['Player']] = player_name

# delete duplicate players on different teams
df = df.drop_duplicates(subset=['Rk'], keep='first')

# delete team after eliminated duplicate players on different teams
del  df['Rk'], df['Tm']

# save modified dataframe to csv
df.to_csv('data/data_set.csv', index=False)