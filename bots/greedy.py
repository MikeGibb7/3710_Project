import sys
import os
import random
import time

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.strategy import Strategy, generateRandomStrategy
from utils.score import calculateScoreTournament
from config import config
from utils.save_strat import save_strategy
from training_set import getHumanTrainingSet

def get_neighbors(strategy):
    """
    Generates a list of neighboring strategies by flipping single moves 
    in the strategy's move_list.
    """
    num_neighbors = 2**(strategy.rounds_in_memory * 2)

    neighbors = []
    
    current_moves = strategy.move_list
    rounds_in_memory = strategy.rounds_in_memory
    
    for index in range(num_neighbors):
        new_moves = current_moves.copy()
        
        flip_index = index
        
        new_moves[flip_index] = 'C' if new_moves[flip_index] == 'D' else 'D'
        
        neighbors.append(Strategy(new_moves, rounds_in_memory, "greedy"))
        
    return neighbors

def train_bot_greedy(training_set, memory_depth, max_execution_time=60, random_restart=0, sideways_moves=True):

    current_bot = generateRandomStrategy(memory_depth)
    best_bot = current_bot
    current_score, _ = calculateScoreTournament(current_bot, training_set=training_set)
    best_score = current_score

    start_time = time.time()
    end_time = start_time + max_execution_time
    # Main Loop

    while time.time() < end_time:

        neighbors = get_neighbors(current_bot)

        best_neighbor = None
        best_neighbor_score = -float('inf')

        for neighbor in neighbors:
            score, _ = calculateScoreTournament(neighbor, training_set=training_set)
            if score > best_neighbor_score:
                best_neighbor = neighbor
                best_neighbor_score = score
            # Allow Sideways moves if enabled
        
        # Move to the best available neighbor
        current_bot = best_neighbor
        current_score = best_neighbor_score

        if current_score > best_score:
            best_bot = current_bot
            best_score = current_score
            print(f"New best Score: {best_score}")

        # add random chance to start from brand new point
        chance = random.random()
        if chance < random_restart:
            current_bot = generateRandomStrategy(memory_depth)
            current_score = calculateScoreTournament(current_bot, training_set=training_set)
    return best_bot, best_score

if __name__ == "__main__":
    MEMORY_DEPTH = 3
    
    print(f"--- Setting up Training Environment (Memory Depth: {MEMORY_DEPTH}) ---")
    training_set = getHumanTrainingSet()

    # Run the Search
    best_strategy, score = train_bot_greedy(
        training_set=training_set,
        memory_depth=MEMORY_DEPTH,
        max_execution_time=180, # How long to train
        random_restart=0.05,
        sideways_moves=True      # How many recent moves to forbid
    )
    
    print("\n--- Training Complete ---")
    print(f"Final High Score: {score}")
    _, individual_scores = calculateScoreTournament(best_strategy, training_set=training_set)
    print("---Individual Scores---")
    overall_scores = 0
    for score in individual_scores:
        print(f"name: " + str(score[0]) + " --- score: " + str(score[1]))
        overall_scores += score[1]
    print(f"Overall Score: {overall_scores}")
    
    # Save the winning strategy!
    save_strategy(best_strategy, filename="greedy_champion.json")