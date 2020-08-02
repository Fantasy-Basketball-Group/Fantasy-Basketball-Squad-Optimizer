import pandas as pd

# import data set
df = pd.read_csv('data/data_set.csv')

# remove player from available and place into roster, returning updated roster
def draft_player(player, roster, avail):
    player_row = avail[avail['Player'] == player]
    updated_roster = roster.append(player_row)
    avail.drop(player_row.index, inplace=True)
    return updated_roster

# generate median player
def median_player(avail):
    d = {
        'Player': ['Mr Median'],
        'FG': [avail['FG'].median()],
        'FGA': [avail['FGA'].median()],
        'FT': [avail['FT'].median()],
        'FTA': [avail['FTA'].median()],
        '3P': [avail['3P'].median()],
        'TRB': [avail['TRB'].median()],
        'AST': [avail['AST'].median()],
        'STL': [avail['STL'].median()],
        'BLK': [avail['BLK'].median()],
        'TOV': [avail['TOV'].median()],
        'PTS': [avail['PTS'].median()]
    }
    median = pd.DataFrame(data=d)
    return median

# generate mean player
def mean_player(avail):
    d = {
        'Player': ['Mr Mean'],
        'FG': [avail['FG'].mean()],
        'FGA': [avail['FGA'].mean()],
        'FT': [avail['FT'].mean()],
        'FTA': [avail['FTA'].mean()],
        '3P': [avail['3P'].mean()],
        'TRB': [avail['TRB'].mean()],
        'AST': [avail['AST'].mean()],
        'STL': [avail['STL'].mean()],
        'BLK': [avail['BLK'].mean()],
        'TOV': [avail['TOV'].mean()],
        'PTS': [avail['PTS'].mean()]
    }
    mean = pd.DataFrame(data=d)
    return mean

roster = pd.DataFrame()
roster = draft_player('Steven Adams', roster, df)
#print(df)
#print(roster)

median = median_player(df)
mean = mean_player(df)
print(median)
print(mean)