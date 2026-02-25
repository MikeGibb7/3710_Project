import sys
import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.strategy import Strategy
from utils.convert import *
from utils.save_strat import *
from utils.score import *
from training_set import getHumanTrainingSet

# Deprecated createTFT

def createTFT(rounds_in_memory,Suspicious=False):
    move_list = []
    counter = 0
    if(Suspicious):
        move_list.append('D')
    else:
        move_list.append('C')
    for x in range(rounds_in_memory - 1):
        move_list.append('C')
    for x in range(2**(rounds_in_memory * 2)):
        binary_encoding = str(bin(counter))
        print(binary_encoding)
        if binary_encoding.endswith('1'):
            move_list.append('D')
        else:
            move_list.append('C')
        counter += 1
    strategy = Strategy(move_list, rounds_in_memory)
    if(Suspicious):
        save_strategy(strategy=strategy, filename="STFT_strategy.json")
    else:
        save_strategy(strategy=strategy, filename="TFT_strategy.json")

def runTFT():
    TFT_Strategy = load_strategy("TFT_strategy.json")
    training_set = getHumanTrainingSet()
    total_score, indivdualScore = calculateScoreTournament(strategy=TFT_Strategy, training_set=training_set)
    return total_score, indivdualScore

if __name__ == "__main__":
    total_score, individual_scores = runTFT()
    print("\n--- Training Complete ---")
    print(f"Final High Score: {total_score}")
    print("---Individual Scores---")
    for score in individual_scores:
        print(f"name: " + str(score[0]) + " --- score: " + str(score[1]))
    