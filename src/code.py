import pandas as pd

# import data set
df = pd.read_csv('data/data_set.csv')
print(df['FG'].size)

# find player by name, return that row
def find_player(player_name, avail):
    return avail[avail['Player'] == player_name]

# remove player from available and place into roster, returning updated roster
def draft_player(player, roster, avail):
    player_row = avail[avail['Player'] == player]
    updated_roster = roster.append(player_row)
    avail.drop(player_row.index, inplace=True)
    return updated_roster

# generate and return median player
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

# generate and return mean player
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

# return net change on a percent stat
def net_change_percent_stat(t_attempts, t_made, p_attempts, p_made):
    after = (t_made + p_made) / (t_attempts + p_attempts)
    before = t_attempts / t_made
    return after - before

# return net change on a counting stat
def net_change_counting_stat(roster, player, counting_stat):
    t_stat = roster[counting_stat].sum()
    p_stat = player[counting_stat].values[0]
    t_size = roster[counting_stat].size
    after = (t_stat + p_stat) / (t_size + 1)
    before = t_stat / t_size
    return after - before

# get net change for field goal percentage
def net_change_fg(roster, player):
    t_fga = roster['FGA'].sum()
    t_fgm = roster['FG'].sum()
    p_fga = player['FGA'].values[0]
    p_fgm = player['FG'].values[0]
    return net_change_percent_stat(t_fga, t_fgm, p_fga, p_fgm)

# get net change for free throw percentage
def net_change_ft(roster, player):
    t_fta = roster['FTA'].sum()
    t_ftm = roster['FT'].sum()
    p_fta = player['FTA'].values[0]
    p_ftm = player['FT'].values[0]
    return net_change_percent_stat(t_fta, t_ftm, p_fta, p_ftm)

# generate a player with net change in stats given potential acquisition
# to a given team, return that player
def net_change_on_acquisition(roster, player):
    d = {
        'Player': [player['Player'].values[0]],
        'NET_FG%': [net_change_fg(roster, player)],
        'NET_FT%': [net_change_ft(roster, player)],
        'NET_3P': [net_change_counting_stat(roster, player, '3P')],
        'NET_TRB': [net_change_counting_stat(roster, player, 'TRB')],
        'NET_AST': [net_change_counting_stat(roster, player, 'AST')],
        'NET_STL': [net_change_counting_stat(roster, player, 'STL')],
        'NET_BLK': [net_change_counting_stat(roster, player, 'BLK')],
        'NET_TOV': [net_change_counting_stat(roster, player, 'TOV') * -1],
        'NET_PTS': [net_change_counting_stat(roster, player, 'PTS')]
    }
    net_change = pd.DataFrame(d)
    return net_change

roster = pd.DataFrame()
roster = draft_player('Stephen Curry', roster, df)
roster = draft_player('LeBron James', roster, df)
roster = draft_player('Giannis Antetokounmpo', roster, df)
player = find_player('Rodney Hood', df)
print(roster)
print(player)
print(net_change_on_acquisition(roster, player))