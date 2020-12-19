import pandas as pd

# Find player by exact name match, return row of that player's data
def find_player(player_name, avail):
    return avail[avail["Player"] == player_name]


# Generate and return mean player
def mean_player(avail):
    d = {
        "Player": ["Mr Mean"],
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
