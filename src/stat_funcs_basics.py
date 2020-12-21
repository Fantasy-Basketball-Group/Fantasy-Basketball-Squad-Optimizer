import pandas as pd

# Gets league data, applies games played weighted percentage
def get_league_data(filename, games_played=True):
    df = pd.read_csv(filename)
    if games_played == False:
        return df
    league_data = pd.DataFrame()
    for i in df.index:
        player = df[df["Player"].index == i]
        gp_weight = player["G"].values[0] / df["G"].max()
        weighted_player = {
            "Player": [player["Player"].values[0]],
            "Pos": [player["Pos"].values[0]],
            "G": [player["G"].values[0]],
            "MP": [player["MP"].values[0] * gp_weight],
            "FGM": [player["FGM"].values[0] * gp_weight],
            "FGA": [player["FGA"].values[0] * gp_weight],
            "FG%": [player["FG%"].values[0]],
            "FTM": [player["FTM"].values[0] * gp_weight],
            "FTA": [player["FTA"].values[0] * gp_weight],
            "FT%": [player["FT%"].values[0]],
            "3PT": [player["3PT"].values[0] * gp_weight],
            "REB": [player["REB"].values[0] * gp_weight],
            "AST": [player["AST"].values[0] * gp_weight],
            "STL": [player["STL"].values[0] * gp_weight],
            "BLK": [player["BLK"].values[0] * gp_weight],
            "TOV": [player["TOV"].values[0] * gp_weight],
            "PTS": [player["PTS"].values[0] * gp_weight], 
        }
        weighted_player_data = pd.DataFrame(weighted_player)
        league_data = league_data.append(weighted_player_data)

    league_data.reset_index(inplace=True, drop=True)
    return league_data 


# Find player by exact name match, return row of that player's data
def find_player(player_name, avail):
    return avail[avail["Player"] == player_name]


# Generate and return mean player
def mean_player(avail):
    d = {
        "Player": ["Mr Mean"],
        "G": [avail["G"].mean()],
        "FGM": [avail["FGM"].mean()],
        "FGA": [avail["FGA"].mean()],
        "FTM": [avail["FTM"].mean()],
        "FTA": [avail["FTA"].mean()],
        "3PT": [avail["3PT"].mean()],
        "REB": [avail["REB"].mean()],
        "AST": [avail["AST"].mean()],
        "STL": [avail["STL"].mean()],
        "BLK": [avail["BLK"].mean()],
        "TOV": [avail["TOV"].mean()],
        "PTS": [avail["PTS"].mean()],
    }
    mean = pd.DataFrame(data=d)
    return mean


# Drafts a player from the available players and into a roster, returning that updated roster
# - removes player from available pool
# - if roster contains a placeholder mean player, it removes it before adding the drafted player
def draft_player(player_name, roster, avail):
    player_row = avail[avail["Player"] == player_name]
    if player_row.empty == True:
        return roster
    if roster.empty == False and "Mr Mean" in roster["Player"].values:
        m_player = roster[roster["Player"] == "Mr Mean"]
        roster.drop(m_player.index, inplace=True)
    roster = roster.append(player_row)
    avail.drop(player_row.index, inplace=True)
    return roster
