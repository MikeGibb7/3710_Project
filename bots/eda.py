import random

from training_set import getHumanTrainingSet
from utils.save_strat import save_strategy
from utils.score import calculateScoreTournament
from utils.strategy import Strategy, generateRandomStrategy


def train_bot_eda(training_set, memory_depth, population_size=50, generations=100):
  # Initialize a population of random strategies
  population = [generateRandomStrategy(memory_depth) for _ in range(population_size)]

  for _ in range(generations):
        
    # Extract the best strategies from the current population
    bots_ranked = []
    for bot in population:
      score = calculateScoreTournament(bot, training_set)
      bots_ranked.append((bot, score))
    
    bots_ranked_indices = sorted(bots_ranked, key=lambda x: x[1], reverse=True) 
    selected_bots_indices = bots_ranked_indices[:population_size // 2]
    selected_bots = [bot for bot, _ in selected_bots_indices]
        
    # Create an array of the odds of choosing 'C' for each move in the strategy
    odds_for_choice_c = []
    for i in range(memory_depth + 2**(memory_depth * 2)):
      count_c = 0
      count_d = 0

      for bot in selected_bots:
        if bot.move_list[i] == 'C':
          count_c += 1
        else:
          count_d += 1

      total = count_c + count_d
      odds_for_choice_c.append(count_c / total)
                               
    # Generate a new population based on the odds of choosing 'C' for each move
    new_population = []
    for _ in range(population_size):
      move_list = []
      for odds in odds_for_choice_c:
        if(random.random() < odds):
          move_list.append('C')
        else:
          move_list.append('D')
      new_population.append(Strategy(move_list, memory_depth))

    population = new_population

  # Get the best strategy from the final population
  bots_ranked = []
  for bot in population:
    score = calculateScoreTournament(bot, training_set)
    bots_ranked.append((bot, score))
    
  bots_ranked_indices = sorted(bots_ranked, key=lambda x: x[1], reverse=True) 
  selected_bots = [bot for bot, _ in bots_ranked_indices]
        
  return bots_ranked_indices[0]

   