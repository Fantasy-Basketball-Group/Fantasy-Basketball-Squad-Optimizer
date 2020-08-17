import sys, os

sys.path.append(os.getcwd() + "/src/")
import stat_funcs as sf
import pandas as pd

df = pd.read_csv("data/test_data_set.csv")


# test to find player successfully
def test_get_player_success():
    avail = df.copy() # generate duplicate data
    player_name = "Stephen Curry"
    player_data = sf.find_player(player_name, avail)
    print(player_data.values[0])
    assert len(player_data.values) == 1  # gets a single player
    assert player_data["Player"].values[0] == player_name  # name is correct
    assert player_data["Pos"].values[0] == "PG"  # position is correct
    assert player_data["MP"].values[0] == 27.8  # minutes played is correct
    assert player_data["FG"].values[0] == 6.6  # fg is correct
    assert player_data["FGA"].values[0] == 16.4  # fga is correct
    assert player_data["FG%"].values[0] == 0.402  # fg% is correct
    assert player_data["3P"].values[0] == 2.4  # 3p is correct
    assert player_data["FT"].values[0] == 5.2  # ft is correct
    assert player_data["FTA"].values[0] == 5.2  # fta is correct
    assert player_data["FT%"].values[0] == 1.0  # ft% is correct
    assert player_data["TRB"].values[0] == 5.2  # trb is correct
    assert player_data["AST"].values[0] == 6.6  # ast is correct
    assert player_data["STL"].values[0] == 1.0  # stl is correct
    assert player_data["BLK"].values[0] == 0.4  # blk is correct
    assert player_data["TOV"].values[0] == 3.2  # tov is correct
    assert player_data["PTS"].values[0] == 20.8  # pts is correct


# test that a player returns an empty data frame
def test_get_player_failure():
    avail = df.copy() # generate duplicate data
    player_name = "Steven Curry"
    player_data = sf.find_player(player_name, avail)
    assert player_data.empty == True


# test that mean player function produces means of all stats
def test_means_player_produces_means():
    avail = df.copy() # generate duplicate data
    mean_player = sf.mean_player(avail)
    assert len(mean_player.values) == 1  # produces a single player
    assert mean_player["Player"].values[0] == "Mr Mean"  # name is correct
    assert mean_player["FG"].values[0] == avail["FG"].mean()  # fg is correct
    assert mean_player["FGA"].values[0] == avail["FGA"].mean()  # fga is correct
    assert mean_player["3P"].values[0] == avail["3P"].mean()  # 3p is correct
    assert mean_player["FT"].values[0] == avail["FT"].mean()  # ft is correct
    assert mean_player["FTA"].values[0] == avail["FTA"].mean()  # fta is correct
    assert mean_player["TRB"].values[0] == avail["TRB"].mean()  # trb is correct
    assert mean_player["AST"].values[0] == avail["AST"].mean()  # ast is correct
    assert mean_player["STL"].values[0] == avail["STL"].mean()  # stl is correct
    assert mean_player["BLK"].values[0] == avail["BLK"].mean()  # blk is correct
    assert mean_player["TOV"].values[0] == avail["TOV"].mean()  # tov is correct
    assert mean_player["PTS"].values[0] == avail["PTS"].mean()  # pts is correct


# test that draft player function removes a player from the given roster and places it into an empty roster
def test_draft_player_to_empty_roster_success():
    empty_roster = pd.DataFrame() # generate empty roster
    assert empty_roster.empty == True # roster is actually empty
    avail = df.copy() # generate duplicate data
    player_name = "Stephen Curry"
    new_roster = sf.draft_player(player_name, empty_roster, avail)
    assert len(avail.values) == len(df.values) - 1 # available players is one less than before
    assert sf.find_player("Stephen Curry", avail).empty == True # the drafted played isn't in available players anymore
    assert len(new_roster.values) == 1 # roster has one player
    assert new_roster["Player"].values[0] == "Stephen Curry" # that player is the one drafted
    