import stat_funcs_basics as sfb
import pandas as pd


class team:
    def __init__(self, owner_name, team_name, df):
        self.owner_name = owner_name
        self.team_name = team_name
        self.roster = sfb.mean_player(df)


class league:
    def __init__(self, league_name, num_of_pl, map_of_league):
        self.league_name = league_name
        self.num_of_pl = num_of_pl
        # Dictionary of team objects mapped by owner_name
        self.map_of_league = map_of_league


def read_league_file(file_name, df):
    map_of_league = {}
    draft_order = {}
    with open(file_name) as file:
        for i, f in enumerate(file):
            lines = f.strip().split("\n")
            # print(lines)
            # print(type(lines))
            for l in lines:
                seg = l.split(",")
                # print(i)

                if (i == 0):  # First line has league name and number of people
                    # print("Here")
                    league_name = seg[0]
                    num_of_pl = seg[1]
                    continue

                cur_team = team(seg[0], seg[1], df)
                # print(cur_team.owner_name)
                # print(cur_team.team_name)
                draft_order[seg[2]] = cur_team.owner_name
                map_of_league[cur_team.owner_name] = cur_team
                # print(map_of_league[cur_team.owner_name].team_name)

    return league(league_name, num_of_pl, map_of_league), draft_order


def display_league(league):
    print("League Name: ", league.league_name)
    print("Member count: ", league.num_of_pl)
    print("Teams:")
    for t in league.map_of_league:
        print(t, "|", league.map_of_league[t].team_name)


# Read in data set
"""
df = pd.read_csv("data/espn_data_set.csv")
my_league, draft_order = read_league_file("data/league.txt", df)
display_league(my_league)
"""
