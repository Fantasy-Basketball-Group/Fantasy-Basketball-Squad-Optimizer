import pandas as pd

# Return net change on a percent stat
def net_change_percent_stat(t_attempts, t_made, p_attempts, p_made):
    after = (t_made + p_made) / (t_attempts + p_attempts)
    before = t_attempts / t_made
    return after - before


# Return net change on a counting stat
def net_change_counting_stat(roster, player, counting_stat):
    t_stat = roster[counting_stat].sum()
    p_stat = player[counting_stat].values[0]
    t_size = roster[counting_stat].size
    after = (t_stat + p_stat) / (t_size + 1)
    before = t_stat / t_size
    return after - before


# Get net change for field goal percentage
def net_change_fg(roster, player):
    t_fga = roster["FGA"].sum()
    t_fgm = roster["FGM"].sum()
    p_fga = player["FGA"].values[0]
    p_fgm = player["FGM"].values[0]
    return net_change_percent_stat(t_fga, t_fgm, p_fga, p_fgm)


# Get net change for free throw percentage
def net_change_ft(roster, player):
    t_fta = roster["FTA"].sum()
    t_ftm = roster["FTM"].sum()
    p_fta = player["FTA"].values[0]
    p_ftm = player["FTM"].values[0]
    return net_change_percent_stat(t_fta, t_ftm, p_fta, p_ftm)


# Generate a player with net change in stats given potential acquisition
# to a given team, return that player
def net_change_on_acquisition(roster, player):
    d = {
        "Player": [player["Player"].values[0]],
        "NET_FG%": [net_change_fg(roster, player)],
        "NET_FT%": [net_change_ft(roster, player)],
        "NET_3PT": [net_change_counting_stat(roster, player, "3PT")],
        "NET_REB": [net_change_counting_stat(roster, player, "REB")],
        "NET_AST": [net_change_counting_stat(roster, player, "AST")],
        "NET_STL": [net_change_counting_stat(roster, player, "STL")],
        "NET_BLK": [net_change_counting_stat(roster, player, "BLK")],
        "NET_TOV": [net_change_counting_stat(roster, player, "TOV") * -1],
        "NET_PTS": [net_change_counting_stat(roster, player, "PTS")],
    }
    net_change = pd.DataFrame(d)
    return net_change


# Generates a table of net change in each stat category for each player available given that they join the roster
def generate_net_change_table(roster, avail):
    net_change_table = pd.DataFrame()
    for i in avail.index:
        player = avail[avail["Player"].index == i]
        net_player = net_change_on_acquisition(roster, player)
        net_change_table = net_change_table.append(net_player)

    net_change_table.reset_index(inplace=True, drop=True)
    return net_change_table
