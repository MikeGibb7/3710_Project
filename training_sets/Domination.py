import sys
import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.strategy import Strategy
from utils.convert import *
from utils.save_strat import save_strategy

def CreateDomination(rounds_in_memory, Comply=True):
    move_list = []
    for x in range(rounds_in_memory + (2**(rounds_in_memory * 2))):
        if(Comply):
            move_list.append('C')
        else:
            move_list.append('D')
    new_strategy = Strategy(move_list, rounds_in_memory=rounds_in_memory)
    if(Comply):
        save_strategy(new_strategy, filename="AllC_strategy.json")
    else:
        save_strategy(new_strategy, filename="AllD_strategy.json")

CreateDomination(1, False)