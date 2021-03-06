import sys, os
from decimal import Decimal as d

sys.path.append(os.getcwd() + "/src/")
import stat_funcs_basics as sfb
import stat_funcs_net as sfn
import pandas as pd

df = pd.read_csv("data/test_data_set.csv")

# NET_CHANGE_PERCENT_STAT TESTS

# test net_change_percent_stat produces correct net change in percentage
def test_net_change_percent_stat():
    avail = df.copy()
    # increase from 37.5% (3/8) to 50% (5/10)
    assert sfn.net_change_percent_stat(3, 8, 2, 2) == 0.125
    # decrease from 40% (4/10) to 25% (4/16)
    assert sfn.net_change_percent_stat(4, 10, 0, 6) == -0.15
