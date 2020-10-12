import pandas as pd

# Generates the standard deviations and means of each stat category
def generate_z_score_dict(net_change_table):
    z_score_dict = {
        # Standard Deviations
        "FG%_std": net_change_table["NET_FG%"].std(),
        "FT%_std": net_change_table["NET_FT%"].std(),
        "3PT_std": net_change_table["NET_3PT"].std(),
        "REB_std": net_change_table["NET_REB"].std(),
        "AST_std": net_change_table["NET_AST"].std(),
        "STL_std": net_change_table["NET_STL"].std(),
        "BLK_std": net_change_table["NET_BLK"].std(),
        "TOV_std": net_change_table["NET_TOV"].std(),
        "PTS_std": net_change_table["NET_PTS"].std(),
        # Means
        "FG%_mean": net_change_table["NET_FG%"].mean(),
        "FT%_mean": net_change_table["NET_FT%"].mean(),
        "3PT_mean": net_change_table["NET_3PT"].mean(),
        "REB_mean": net_change_table["NET_REB"].mean(),
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
        "Z_3PT": [
            z_score(
                net_player["NET_3PT"].values[0],
                z_score_dict["3PT_mean"],
                z_score_dict["3PT_std"],
            )
        ],
        "Z_REB": [
            z_score(
                net_player["NET_REB"].values[0],
                z_score_dict["REB_mean"],
                z_score_dict["REB_std"],
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
    z_total = (
        d["Z_FG%"][0]
        + d["Z_FT%"][0]
        + d["Z_3PT"][0]
        + d["Z_REB"][0]
        + d["Z_AST"][0]
        + d["Z_STL"][0]
        + d["Z_BLK"][0]
        + d["Z_TOV"][0]
        + d["Z_PTS"][0]
    )
    d.update({"Z_AVG": [z_total / 9]})
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


# prints the top n players from a given category
def print_top_n(table, column_label, n):
    if column_label not in list(table.columns.values):
        return False
    sorted_table = table.sort_values(by=[column_label], ascending=False)
    sorted_table.reset_index(inplace=True, drop=True)
    sorted_table.drop(sorted_table.index[n:], inplace=True)
    print(sorted_table)
    return True
