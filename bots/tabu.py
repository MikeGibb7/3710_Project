import sys
import os
import random

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from utils.strategy import Strategy, generateRandomStrategy
from utils.score import calculateScoreTournament
from config import config
from utils.save_strat import save_strategy

def get_neighbors(strategy, num_neighbors=10):
    """
    Generates a list of neighboring strategies by flipping single moves 
    in the strategy's move_list.
    """
    neighbors = []
    
    current_moves = strategy.move_list
    rounds_in_memory = strategy.rounds_in_memory
    
    for _ in range(num_neighbors):
        new_moves = current_moves.copy()
        
        flip_index = random.randint(0, len(new_moves) - 1)
        
        new_moves[flip_index] = 'C' if new_moves[flip_index] == 'D' else 'D'
        
        neighbors.append(Strategy(new_moves, rounds_in_memory))
        
    return neighbors

def strategy_to_string(strategy):
    return "".join(strategy.move_list)

# --- TABU SEARCH ALGORITHM ---

def train_bot_tabu(training_set, memory_depth, max_iterations=200, tabu_tenure=15, num_neighbors=20):
    """
    Optimizes a strategy using Tabu Search to beat the provided training_set.
    """
    # 1. Generate a random starting point
    current_bot = generateRandomStrategy(memory_depth)
    best_bot = current_bot
    
    current_score = calculateScoreTournament(current_bot, training_set)
    best_score = current_score
    
    tabu_list = [] # Stores string IDs of visited strategies

    # 2. Main Search Loop
    for iteration in range(max_iterations):
        neighbors = get_neighbors(current_bot, num_neighbors=num_neighbors)
        
        best_neighbor = None
        best_neighbor_score = -float('inf')
        
        # Evaluate all neighbors
        for neighbor in neighbors:
            neighbor_id = strategy_to_string(neighbor)
            
            score = calculateScoreTournament(neighbor, training_set)
            
            is_tabu = neighbor_id in tabu_list
            
            # Aspiration Criterion: Ignore Tabu status if we found a new global best
            if is_tabu and score > best_score:
                is_tabu = False
                
            # Select the best neighbor that is strictly non-Tabu (or satisfied Aspiration)
            if not is_tabu and score > best_neighbor_score:
                best_neighbor = neighbor
                best_neighbor_score = score
        
        # If no valid neighbors found (rare, but possible if all are Tabu and worse)
        if best_neighbor is None:
            print(f"No valid neighbors found at iteration {iteration}. Stopping.")
            break
            
        # 3. Move to the best neighbor
        current_bot = best_neighbor
        current_score = best_neighbor_score
        
        # 4. Update Global Best
        if current_score > best_score:
            best_bot = current_bot
            best_score = current_score
            print(f"[{iteration}] New Best Score: {best_score}")
            
        # 5. Update Tabu List
        tabu_list.append(strategy_to_string(current_bot))
        if len(tabu_list) > tabu_tenure:
            tabu_list.pop(0) # Remove oldest entry (FIFO)

    return best_bot, best_score

# --- EXECUTION ---

if __name__ == "__main__":
    MEMORY_DEPTH = 2
    
    print(f"--- Setting up Training Environment (Memory Depth: {MEMORY_DEPTH}) ---")
    training_set = []
    for _ in range(20):
        training_set.append(generateRandomStrategy(random.choice([1, 2, 3])))

    # Run the Search
    best_strategy, score = train_bot_tabu(
        training_set=training_set,
        memory_depth=MEMORY_DEPTH,
        max_iterations=100, # How long to train
        tabu_tenure=10      # How many recent moves to forbid
    )
    
    print("\n--- Training Complete ---")
    print(f"Final High Score: {score}")
    
    # Save the winning strategy!
    save_strategy(best_strategy, filename="tabu_champion.json")