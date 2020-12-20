import stat_funcs_basics as sfb
import stat_funcs_net as sfn
import stat_funcs_z as sfz
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# Generate z score data
df = pd.read_csv("data/espn_data_set.csv")
roster = sfb.mean_player(df)
net_change_table = sfn.generate_net_change_table(roster, df)
z_score_table = sfz.generate_z_score_table(net_change_table)

# Select data parameter & print table
stat_str = "Z_AVG"
z_score_table.sort_values(by=[stat_str], ascending=False, inplace=True)
#z_score_table.to_csv("data/z_score_table.csv", index=False)
print(net_change_table)
print(z_score_table)


for stat_str in z_score_table:
    # Create matplotlib histogram
    if stat_str == "Player":
        continue
    z_avg_array = z_score_table[stat_str].to_numpy()
    num_bins = 25
    n, bins, patches = plt.hist(z_avg_array, num_bins)
    ax = plt.gca()
    ax.yaxis.set_major_formatter(PercentFormatter(n.sum()))
    ax.set_ylabel("Percentage of Players")
    ax.set_xlabel("Standard Deviations from Mean")

    plt.title("Distribution " + stat_str)
    plt.show()
