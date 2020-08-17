import sys, os

sys.path.append(os.getcwd() + "/src/")
import stat_funcs as sf
import pandas as pd

df = pd.read_csv("data/test_data_set.csv")


# test to find player successfully
def test_get_player_success():
    player_name = "Stephen Curry"
    player_data = sf.find_player(player_name, df)
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
    player_name = "Steven Curry"
    player_data = sf.find_player(player_name, df)
    assert len(player_data.values) == 0
