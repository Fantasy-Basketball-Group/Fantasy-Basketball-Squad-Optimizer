import stat_funcs_basics as sfb
import league as lg
import pandas as pd


class draft:
    def __init__(self, league, player_pool, draft_order, already_drafted):
        self.league = league
        self.player_pool = player_pool
        self.draft_order = draft_order
        self.already_drafted = already_drafted
