import stat_funcs_basics as sfb
import stat_funcs_net as sfn
import stat_funcs_z as sfz
import league as lg
import pandas as pd

pd.set_option("display.max_rows", None, "display.max_columns", None)

# Generates Z scores for all available player if added to roster
def optimizer_analysis2(roster, draft_pool):
    net_change_table = sfn.generate_net_change_table(roster, draft_pool)
    z_score_table = sfz.generate_z_score_table(net_change_table)
    z_score_table.sort_values(by=["Z_AVG"], ascending=False, inplace=True)
    print(z_score_table.to_string())
    return


# Return net change on a percent stat
# - rounds result to nearest 4 decimal places
def change_percent_stat(t_made, t_attempts, p_made, p_attempts):
    # shooting percentage after player acquisition
    after = (t_made + p_made) / (t_attempts + p_attempts)
    return round(after, 4)


# Get net change for field goal percentage
def change_fg(roster, player):
    t_fga = roster["FGA"].sum()
    t_fgm = roster["FGM"].sum()
    p_fga = player["FGA"].values[0]
    p_fgm = player["FGM"].values[0]
    return change_percent_stat(t_fgm, t_fga, p_fgm, p_fga)


# Get net change for free throw percentage
def change_ft(roster, player):
    t_fta = roster["FTA"].sum()
    t_ftm = roster["FTM"].sum()
    p_fta = player["FTA"].values[0]
    p_ftm = player["FTM"].values[0]
    return change_percent_stat(t_ftm, t_fta, p_ftm, p_fta)


# Return net change on a counting stat
def change_counting_stat(roster, player, counting_stat):
    t_stat = roster[counting_stat].sum()
    p_stat = player[counting_stat].values[0]
    t_size = roster[counting_stat].size
    after = (t_stat + p_stat) / (t_size + 1)
    return after


# Return the net change to the team when a player is added
def change_on_acquisition(roster, player):
    d = {
        "Player": [player["Player"].values[0]],
        "NET_FG%": [change_fg(roster, player)],
        "NET_FT%": [change_ft(roster, player)],
        "NET_3PT": [change_counting_stat(roster, player, "3PT")],
        "NET_REB": [change_counting_stat(roster, player, "REB")],
        "NET_AST": [change_counting_stat(roster, player, "AST")],
        "NET_STL": [change_counting_stat(roster, player, "STL")],
        "NET_BLK": [change_counting_stat(roster, player, "BLK")],
        "NET_TOV": [change_counting_stat(roster, player, "TOV") * -1],
        "NET_PTS": [change_counting_stat(roster, player, "PTS")],
    }
    net_change = pd.DataFrame(d)
    return net_change


def analyze_roster(roster, player_pool):
    ex = False
    while ex == False:
        print("Analysis Menu: ")
        print("1. Add Player")
        print("2. Display Roster")
        print("3. Net Change for Player")
        print("4. Optimizer Analysis")
        print("5. Quit")
        choice = input()

        if choice == "1":
            player_name = input("Who would you like to add? ")
            roster = sfb.draft_player(player_name, roster, player_pool)
        elif choice == "2":
            print(roster.to_string())
        elif choice == "3":
            player_name = input("Who would you like to check if on your team? ")
            player = sfb.find_player(player_name, player_pool)
            print("Change to team:")
            print(change_on_acquisition(roster, player).to_string())
            print("Net Change with player:")
            print(sfn.net_change_on_acquisition(roster, player).to_string())
        elif choice == "4":
            optimizer_analysis2(roster, player_pool)
        elif choice == "5":
            ex = True

    return


df = pd.read_csv("data/espn_data_set.csv")
roster = sfb.mean_player(df)
analyze_roster(roster, df)
