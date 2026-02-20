import json
import os
from utils.strategy import Strategy

def save_strategy(strategy, filename):
    data_to_save = {
        "rounds_in_memory": strategy.rounds_in_memory,
        "move_list": strategy.move_list
    }
    
    os.makedirs("saved_bots", exist_ok=True)
    filepath = os.path.join("saved_bots", filename)
    
    with open(filepath, 'w') as json_file:
        json.dump(data_to_save, json_file, indent=4)

def load_strategy(filename):

    filepath = os.path.join("saved_bots", filename)
    
    if not os.path.exists(filepath):
        print(f"Error: Could not find {filepath}")
        return None
        
    with open(filepath, 'r') as json_file:
        loaded_data = json.load(json_file)
        
    return Strategy(
        strategy=loaded_data["move_list"], 
        rounds_in_memory=loaded_data["rounds_in_memory"]
    )