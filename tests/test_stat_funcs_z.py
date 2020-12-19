import sys, os

sys.path.append(os.getcwd() + "/src/")
import stat_funcs_z as sf
import pandas as pd

df = pd.read_csv("data/test_data_set.csv")
