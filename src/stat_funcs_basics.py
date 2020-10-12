import pandas as pd

# Find player by name, return that row
def find_player(player_name, avail):
    return avail[avail["Player"] == player_name]


# Remove player from available and place into roster, returning updated roster
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