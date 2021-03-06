import sys, os

sys.path.append(os.getcwd() + "/src/")
import stat_funcs_basics as sfb
import pandas as pd

df = pd.read_csv("data/test_data_set.csv")

# GET_LEAGUE_DATA TESTS

# test to import data correctly, flag off
def test_get_league_data_flag_off():
    league_data = sfb.get_league_data("data/test_data_set.csv", False)
    assert league_data.equals(df)


# test to import data correctly, flag on
def test_get_league_data_flag_on():
    league_data = sfb.get_league_data("data/test_data_set.csv")
    avail = df.copy()
    player_name = "Stephen Curry"
    player_data = sfb.find_player(player_name, league_data)
    gp_percentage = player_data["G"].values[0] / avail["G"].max()
    assert len(player_data.values) == 1  # gets a single player
    assert player_data["Player"].values[0] == player_name  # name is correct
    assert player_data["Pos"].values[0] == "PG"  # position is correct
    assert player_data["G"].values[0] == 5  # games played is correct
    assert (
        player_data["MP"].values[0] == 27.8 * gp_percentage
    )  # minutes played is correct
    assert player_data["FGM"].values[0] == 6.6 * gp_percentage  # fgm is correct
    assert player_data["FGA"].values[0] == 16.4 * gp_percentage  # fga is correct
    assert player_data["FG%"].values[0] == 0.402  # fg% is correct
    assert player_data["3PT"].values[0] == 2.4 * gp_percentage  # 3pt is correct
    assert player_data["FTM"].values[0] == 5.2 * gp_percentage  # ftm is correct
    assert player_data["FTA"].values[0] == 5.2 * gp_percentage  # fta is correct
    assert player_data["FT%"].values[0] == 1.0  # ft% is correct
    assert player_data["REB"].values[0] == 5.2 * gp_percentage  # reb is correct
    assert player_data["AST"].values[0] == 6.6 * gp_percentage  # ast is correct
    assert player_data["STL"].values[0] == 1.0 * gp_percentage  # stl is correct
    assert player_data["BLK"].values[0] == 0.4 * gp_percentage  # blk is correct
    assert player_data["TOV"].values[0] == 3.2 * gp_percentage  # tov is correct
    assert player_data["PTS"].values[0] == 20.8 * gp_percentage  # pts is correct


# FIND_PLAYER TESTS

# test to find player successfully
def test_find_player_success():
    avail = df.copy()  # generate duplicate data
    player_name = "Stephen Curry"
    player_data = sfb.find_player(player_name, avail)
    assert len(player_data.values) == 1  # gets a single player
    assert player_data["Player"].values[0] == player_name  # name is correct
    assert player_data["Pos"].values[0] == "PG"  # position is correct
    assert player_data["G"].values[0] == 5  # games played is correct
    assert player_data["MP"].values[0] == 27.8  # minutes played is correct
    assert player_data["FGM"].values[0] == 6.6  # fgm is correct
    assert player_data["FGA"].values[0] == 16.4  # fga is correct
    assert player_data["FG%"].values[0] == 0.402  # fg% is correct
    assert player_data["3PT"].values[0] == 2.4  # 3pt is correct
    assert player_data["FTM"].values[0] == 5.2  # ftm is correct
    assert player_data["FTA"].values[0] == 5.2  # fta is correct
    assert player_data["FT%"].values[0] == 1.0  # ft% is correct
    assert player_data["REB"].values[0] == 5.2  # reb is correct
    assert player_data["AST"].values[0] == 6.6  # ast is correct
    assert player_data["STL"].values[0] == 1.0  # stl is correct
    assert player_data["BLK"].values[0] == 0.4  # blk is correct
    assert player_data["TOV"].values[0] == 3.2  # tov is correct
    assert player_data["PTS"].values[0] == 20.8  # pts is correct


# test that a player returns an empty data frame
def test_find_player_failure():
    avail = df.copy()  # generate duplicate data
    player_name = "Steven Curry"
    player_data = sfb.find_player(player_name, avail)
    assert player_data.empty == True


# MEAN_PLAYER TESTS

# test that mean player function produces means of all stats
def test_means_player_produces_means():
    avail = df.copy()  # generate duplicate data
    mean_player = sfb.mean_player(avail)
    assert len(mean_player.values) == 1  # produces a single player
    assert mean_player["Player"].values[0] == "Mr Mean"  # name is correct
    assert mean_player["G"].values[0] == avail["G"].mean()  # g is correct
    assert mean_player["FGM"].values[0] == avail["FGM"].mean()  # fgm is correct
    assert mean_player["FGA"].values[0] == avail["FGA"].mean()  # fga is correct
    assert mean_player["3PT"].values[0] == avail["3PT"].mean()  # 3pt is correct
    assert mean_player["FTM"].values[0] == avail["FTM"].mean()  # ftm is correct
    assert mean_player["FTA"].values[0] == avail["FTA"].mean()  # fta is correct
    assert mean_player["REB"].values[0] == avail["REB"].mean()  # reb is correct
    assert mean_player["AST"].values[0] == avail["AST"].mean()  # ast is correct
    assert mean_player["STL"].values[0] == avail["STL"].mean()  # stl is correct
    assert mean_player["BLK"].values[0] == avail["BLK"].mean()  # blk is correct
    assert mean_player["TOV"].values[0] == avail["TOV"].mean()  # tov is correct
    assert mean_player["PTS"].values[0] == avail["PTS"].mean()  # pts is correct


# DRAFT_PLAYER TESTS

# test that draft player function removes a player from the given roster and places it into an empty roster
def test_draft_player_to_empty_roster_success():
    avail = df.copy()  # generate duplicate data
    empty_roster = pd.DataFrame()  # generate empty roster
    player_name = "Stephen Curry"
    new_roster = sfb.draft_player(player_name, empty_roster, avail)
    assert (
        len(avail.values) == len(df.values) - 1
    )  # available players is one less than before
    assert (
        sfb.find_player("Stephen Curry", avail).empty == True
    )  # the drafted played isn't in available players anymore
    assert len(new_roster.values) == 1  # roster has one player
    assert (
        new_roster["Player"].values[0] == "Stephen Curry"
    )  # that player is the one drafted


# test that draft player function doesn't make any modifications on fail to find
def test_draft_player_to_empty_roster_fail_to_find():
    avail = df.copy()
    empty_roster = pd.DataFrame()
    mean_player = sfb.mean_player(avail)
    single_player = sfb.find_player("Damian Lillard", avail)
    player_name = "Steven Curry"
    assert sfb.draft_player(player_name, empty_roster, avail).equals(
        empty_roster
    )  # empty unchanged
    assert sfb.draft_player(player_name, mean_player, avail).equals(
        mean_player
    )  # mean unchanged
    assert sfb.draft_player(player_name, single_player, avail).equals(
        single_player
    )  # single unchanged
    assert avail.equals(df)  # avail unchanged


# test that draft player function success for empty roster
def test_draft_player_to_empty_success():
    avail = df.copy()
    empty_roster = pd.DataFrame()
    player_name = "Stephen Curry"
    new_roster = sfb.draft_player(player_name, empty_roster, avail)
    assert (
        len(avail.values) == len(df.values) - 1
    )  # size of available players decreases by 1
    assert (
        sfb.find_player(player_name, avail).empty == True
    )  # drafted player no longer available
    assert len(new_roster.values) == 1  # new roster has exactly one player in it
    assert (
        new_roster["Player"].values[0] == player_name
    )  # that player is the one that was drafted


# test that draft player function success for mean player in roster
def test_draft_player_to_mean_player_roster():
    avail = df.copy()
    mean_player = sfb.mean_player(avail)
    player_name = "Stephen Curry"
    new_roster = sfb.draft_player(player_name, mean_player, avail)
    assert (
        len(avail.values) == len(df.values) - 1
    )  # size of available players decreases by 1
    assert (
        sfb.find_player(player_name, avail).empty == True
    )  # drafted player no longer available
    assert len(new_roster.values) == 1  # new roster has exactly one player in it
    assert (
        new_roster["Player"].values[0] == player_name
    )  # that player is the one that was drafted
    assert (
        sfb.find_player("Mr Mean", new_roster).empty == True
    )  # mean player no longer on roster
