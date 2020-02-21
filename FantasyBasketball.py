# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 11:55:14 2019

@author: Santiago
"""
import numpy as np
from numpy.random import choice
import pandas as pd
import math
import csv

#class player:
#    def __init__(self, name, team, position, pts, reb, ast, blk, stl, fg%, ft%, 3pm, gp, mins, to):
#        self.team = team
#        self.position = position
#        self.pts = pts #points
#        self.reb = reb #rebounds
#        self.ast = ast #assists
#        self.blk = blk #blocks
#        self.stl = stl #steals
#        self.fg% = fg% #field goal percentage
#        self.ft% = ft% #free throw percentage
#        self.3pm = 3pm #three pointers made
#        self.gp = gp #games played
#        self.mins = mins #minutes
#        self.to = to #turnovers
   
#    def display_player(self):
#        print(self.name, self.team, self.position) 
#        print("FG%:", self.fg%, "FT%;", self.ft%, "3-pointers:", self.3pm, "games played:", self.gp, "mins:", self.mins)
#        print("points:", self.pts, "rebounds:", self.reb, "assists:", self.ast, "blocks:", self.blk, "steals:", self.stl, "turnovers:", self.to)


def ReadFromFile():
    draft_pool = pd.read_csv('FantasyPros_Fantasy_Basketball_Overall_2019_Projections.csv')
    return draft_pool

def RemovePlayer(draft_pool, pname):
    indices = draft_pool[draft_pool['Player'] == pname].index
#    print("indices:", indices)
    draft_pool.drop(indices, inplace=True)
    
def main ()  : 
    draft_pool = ReadFromFile()
    print ("Welcome to NBA Fantasy Basketball!!!")
    Quit = False
    while (Quit != True):
        print("Main Menu:")
        print ("1.View Draft Pool")
        print ("2.Remove player from Draft Pool")
        print ("3.Quit")
        pick = input()
        
        if (pick == '1'):
            print(draft_pool)
        elif (pick == '2'):
            pname = input("Who would you like to remove ")
            RemovePlayer(draft_pool, pname)
        else:
            return
        
        
main()
        
        
    
    
    
    
