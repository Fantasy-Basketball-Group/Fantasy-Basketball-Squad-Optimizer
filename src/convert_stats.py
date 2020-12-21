import pandas as pd
import numpy as np

df = pd.read_csv("data/made_attempts.csv")
fgm_list = list()
fga_list = list()
ftm_list = list()
fta_list = list()

for ind in df.index:
    fgm = df["FG"][ind].split("/")[0]
    fgm_list.append(fgm)
    fga = df["FG"][ind].split("/")[1]
    fga_list.append(fga)
    ftm = df["FT"][ind].split("/")[0]
    ftm_list.append(ftm)
    fta = df["FT"][ind].split("/")[1]
    fta_list.append(fta)

df.insert(2, "FGM", fgm_list)
df.insert(3, "FGA", fga_list)
df.insert(4, "FTM", ftm_list)
df.insert(5, "FTA", fta_list)

# save modified dataframe to csv
df.to_csv("data/made_attempts_2.csv", index=False)
