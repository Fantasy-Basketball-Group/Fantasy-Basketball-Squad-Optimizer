import stat_funcs_basics as sfb
import stat_funcs_net as sfn
import stat_funcs_z as sfz
import league as lg
import pandas as pd
pd.set_option("display.max_rows", None, "display.max_columns", None)


class draft:
    def __init__(self, league, num_of_rounds, player_pool, draft_order, already_drafted):
        self.league = league
        self.num_of_rounds = num_of_rounds
        self.player_pool = player_pool  # dictionary of available players
        self.draft_order = draft_order  # dictionary of draft order
        self.already_drafted = already_drafted  # dictionary of already drafted players


def draft_menu():
    print("Draft Menu: ")
    print("1. Draft Player")
    print("2. Available Players")
    print("3. Already Drafted")
    print("4. Individual Roster")
    print("5. Optimizer Analysis")
    print("6. Quit")
    choice = input()
    return choice


def optimizer_analysis(roster, draft_pool):
    net_change_table = sfn.generate_net_change_table(roster, draft_pool)
    z_score_table = sfz.generate_z_score_table(net_change_table)
    z_score_table.sort_values(by=["Z_AVG"], ascending=False, inplace=True)
    return z_score_table


def simulate_draft(draft):
    print("Welcome to your Fantasy Basketball Draft")
    pick = 1
    total_picks = int(draft.league.num_of_pl) * int(draft.num_of_rounds)
    while(pick <= total_picks):
        on_clock = draft.draft_order[str(pick % int(draft.league.num_of_pl))]
        print(on_clock, "is on the clock!")
        choice = draft_menu()
        if (choice == "1"):  # Draft Player
            player_name = input("Who would you like to draft? ")
            draft.league.map_of_league[on_clock].roster = sfb.draft_player(
                player_name, draft.league.map_of_league[on_clock].roster, draft.player_pool)
            draft.already_drafted[pick] = player_name
            print("#################################################################")
            print("With the", pick, "pick in the draft,",
                  on_clock, "selects", player_name)
            print("#################################################################")
            pick += 1
        elif (choice == "2"):  # Avaliable Players
            print(draft.player_pool.to_string())
        elif (choice == "3"):  # Already Drafted
            print(draft.already_drafted)
        elif (choice == "4"):  # Individual Roster
            team_owner = input("Who's team would you like to see?")
            print(team_owner,
                  draft.league.map_of_league[team_owner].roster.to_string())
        elif (choice == "5"):  # Optimizer Analysis
            print(optimizer_analysis(
                draft.league.map_of_league[on_clock].roster, draft.player_pool).to_string())
        elif (choice == "6"):  # Quit
            break
    print("And that concludes the draft!!")
    return


player_pool = pd.read_csv("data/espn_data_set.csv")
my_league, draft_order, num_of_rounds = lg.read_league_file(
    "data/league.txt", player_pool)
already_drafted = {}
draft = draft(my_league, num_of_rounds, player_pool,
              draft_order, already_drafted)
simulate_draft(draft)
