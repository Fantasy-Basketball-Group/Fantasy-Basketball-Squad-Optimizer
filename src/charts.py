import stat_funcs as sf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

# Generate z score data
df = pd.read_csv("data/data_set.csv")
roster = sf.mean_player(df)
net_change_table = sf.generate_net_change_table(roster, df)
z_score_table = sf.generate_z_score_table(net_change_table)

# Select data parameter & print table
stat_str = "Z_FT%"
z_score_table.sort_values(by=[stat_str], ascending=False, inplace=True)
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
