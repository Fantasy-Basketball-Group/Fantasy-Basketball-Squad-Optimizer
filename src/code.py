import pandas as pd

# import data set
df = pd.read_csv("data/data_set.csv")
# print(df['FG'].size)

# Find player by name, return that row
def find_player(player_name, avail):
    return avail[avail["Player"] == player_name]


# Remove player from available and place into roster, returning updated roster
def draft_player(player, roster, avail):
    player_row = avail[avail["Player"] == player]
    updated_roster = roster.append(player_row)
    avail.drop(player_row.index, inplace=True)
    return updated_roster


# Generate and return median player
def median_player(avail):
    d = {
        "Player": ["Mr Median"],
        "FG": [avail["FG"].median()],
        "FGA": [avail["FGA"].median()],
        "FT": [avail["FT"].median()],
        "FTA": [avail["FTA"].median()],
        "3P": [avail["3P"].median()],
        "TRB": [avail["TRB"].median()],
        "AST": [avail["AST"].median()],
        "STL": [avail["STL"].median()],
        "BLK": [avail["BLK"].median()],
        "TOV": [avail["TOV"].median()],
        "PTS": [avail["PTS"].median()],
    }
    median = pd.DataFrame(data=d)
    return median


# Generate and return mean player
def mean_player(avail):
    d = {
        "Player": ["Mr Mean"],
        "FG": [avail["FG"].mean()],
        "FGA": [avail["FGA"].mean()],
        "FT": [avail["FT"].mean()],
        "FTA": [avail["FTA"].mean()],
        "3P": [avail["3P"].mean()],
        "TRB": [avail["TRB"].mean()],
        "AST": [avail["AST"].mean()],
        "STL": [avail["STL"].mean()],
        "BLK": [avail["BLK"].mean()],
        "TOV": [avail["TOV"].mean()],
        "PTS": [avail["PTS"].mean()],
    }
    mean = pd.DataFrame(data=d)
    return mean


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
    t_fgm = roster["FG"].sum()
    p_fga = player["FGA"].values[0]
    p_fgm = player["FG"].values[0]
    return net_change_percent_stat(t_fga, t_fgm, p_fga, p_fgm)


# Get net change for free throw percentage
def net_change_ft(roster, player):
    t_fta = roster["FTA"].sum()
    t_ftm = roster["FT"].sum()
    p_fta = player["FTA"].values[0]
    p_ftm = player["FT"].values[0]
    return net_change_percent_stat(t_fta, t_ftm, p_fta, p_ftm)


# Generate a player with net change in stats given potential acquisition
# to a given team, return that player
def net_change_on_acquisition(roster, player):
    d = {
        "Player": [player["Player"].values[0]],
        "NET_FG%": [net_change_fg(roster, player)],
        "NET_FT%": [net_change_ft(roster, player)],
        "NET_3P": [net_change_counting_stat(roster, player, "3P")],
        "NET_TRB": [net_change_counting_stat(roster, player, "TRB")],
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


# Generates the standard deviations and means of each stat category
def generate_z_score_dict(net_change_table):
    z_score_dict = {
        # Standard Deviations
        "FG%_std": net_change_table["NET_FG%"].std(),
        "FT%_std": net_change_table["NET_FT%"].std(),
        "3P_std": net_change_table["NET_3P"].std(),
        "TRB_std": net_change_table["NET_TRB"].std(),
        "AST_std": net_change_table["NET_AST"].std(),
        "STL_std": net_change_table["NET_STL"].std(),
        "BLK_std": net_change_table["NET_BLK"].std(),
        "TOV_std": net_change_table["NET_TOV"].std(),
        "PTS_std": net_change_table["NET_PTS"].std(),
        # Means
        "FG%_mean": net_change_table["NET_FG%"].mean(),
        "FT%_mean": net_change_table["NET_FT%"].mean(),
        "3P_mean": net_change_table["NET_3P"].mean(),
        "TRB_mean": net_change_table["NET_TRB"].mean(),
        "AST_mean": net_change_table["NET_AST"].mean(),
        "STL_mean": net_change_table["NET_STL"].mean(),
        "BLK_mean": net_change_table["NET_BLK"].mean(),
        "TOV_mean": net_change_table["NET_TOV"].mean(),
        "PTS_mean": net_change_table["NET_PTS"].mean(),
    }
    return z_score_dict


# Calculates z score
def z_score(x, mean, std):
    return (x - mean) / std


# Generates player with their z scores for each stat category based on net change
def generate_z_score_player(net_player, z_score_dict):
    d = {
        "Player": [net_player["Player"].values[0]],
        "Z_FG%": [
            z_score(
                net_player["NET_FG%"].values[0],
                z_score_dict["FG%_mean"],
                z_score_dict["FG%_std"],
            )
        ],
        "Z_FT%": [
            z_score(
                net_player["NET_FT%"].values[0],
                z_score_dict["FT%_mean"],
                z_score_dict["FT%_std"],
            )
        ],
        "Z_3P": [
            z_score(
                net_player["NET_3P"].values[0],
                z_score_dict["3P_mean"],
                z_score_dict["3P_std"],
            )
        ],
        "Z_TRB": [
            z_score(
                net_player["NET_TRB"].values[0],
                z_score_dict["TRB_mean"],
                z_score_dict["TRB_std"],
            )
        ],
        "Z_AST": [
            z_score(
                net_player["NET_AST"].values[0],
                z_score_dict["AST_mean"],
                z_score_dict["AST_std"],
            )
        ],
        "Z_STL": [
            z_score(
                net_player["NET_STL"].values[0],
                z_score_dict["STL_mean"],
                z_score_dict["STL_std"],
            )
        ],
        "Z_BLK": [
            z_score(
                net_player["NET_BLK"].values[0],
                z_score_dict["BLK_mean"],
                z_score_dict["BLK_std"],
            )
        ],
        "Z_TOV": [
            z_score(
                net_player["NET_TOV"].values[0],
                z_score_dict["TOV_mean"],
                z_score_dict["TOV_std"],
            )
        ],
        "Z_PTS": [
            z_score(
                net_player["NET_PTS"].values[0],
                z_score_dict["PTS_mean"],
                z_score_dict["PTS_std"],
            )
        ],
    }
    d.update(
        {
            "Z_TOT": [
                d["Z_FG%"][0]
                + d["Z_FT%"][0]
                + d["Z_3P"][0]
                + d["Z_TRB"][0]
                + d["Z_AST"][0]
                + d["Z_STL"][0]
                + d["Z_BLK"][0]
                + d["Z_TOV"][0]
                + d["Z_PTS"][0]
            ]
        }
    )

    d.update({"Z_AVG": [d["Z_TOT"][0] / 9]})
    z_score_player = pd.DataFrame(d)
    return z_score_player


# Generates the z score table using net change table
def generate_z_score_table(net_change_table):
    z_score_dict = generate_z_score_dict(net_change_table)
    z_score_table = pd.DataFrame()
    for i in net_change_table.index:
        net_player = net_change_table[net_change_table["Player"].index == i]
        z_player = generate_z_score_player(net_player, z_score_dict)
        z_score_table = z_score_table.append(z_player)

    z_score_table.sort_values(by=["Z_AVG"], ascending=False, inplace=True)
    z_score_table.reset_index(inplace=True, drop=True)
    return z_score_table


# roster = pd.DataFrame()
# roster = draft_player('Stephen Curry', roster, df)
# roster = draft_player('LeBron James', roster, df)
# roster = draft_player('Giannis Antetokounmpo', roster, df)
roster = mean_player(df)
net_change_table = generate_net_change_table(roster, df)
z_score_table = generate_z_score_table(net_change_table)
# print(find_player("Draymond Green", z_score_table))
print(z_score_table)
# player = find_player('Rodney Hood', df)
# #print(roster)
# print(player)
# #print(net_change_on_acquisition(roster, player))
