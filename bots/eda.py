import random

from training_set import getHumanTrainingSet
from utils.save_strat import save_strategy
from utils.score import calculateScoreTournament
from utils.strategy import Strategy, generateRandomStrategy, printAllStrategies


def train_bot_eda(training_set, memory_depth, population_size, generations):
  # Initialize a population of random strategies
  population = [generateRandomStrategy(memory_depth) for _ in range(population_size)]
  # print("Initial population:")
  # print(len(population))
  # printAllStrategies(population)

  for _ in range(generations):
        
    # Extract the best strategies from the current population
    population_with_scores = []
    for bot in population:
      score, _ = calculateScoreTournament(bot, training_set)
      population_with_scores.append((bot, score))
    
    population_with_scores_ranked = sorted(population_with_scores, key=lambda x: x[1], reverse=True) 
    population_with_scores_trimmed = population_with_scores_ranked[:population_size // 2]
    best_of_population = [bot for bot, _ in population_with_scores_trimmed]

    # print("Best of population:")
    # printAllStrategies(best_of_population)
        
    # Create an array of the odds of choosing 'C' for each move in the strategy
    odds_for_choice_c = []
    for i in range(memory_depth + 2**(memory_depth * 2)):
      count_c = 0
      count_d = 0

      for bot in best_of_population:
        if bot.move_list[i] == 'C':
          count_c += 1
        else:
          count_d += 1

      total = count_c + count_d
      odds_for_choice_c.append(count_c / total)

    # print("Odds of each choice:")
    # print(odds_for_choice_c)
                               
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

    # print("New population:")
    # printAllStrategies(population)

  # Get the best strategy from the final population
  population_with_scores = []
  for bot in population:
    score, _ = calculateScoreTournament(bot, training_set)
    population_with_scores.append((bot, score))
  population_with_scores_ranked = sorted(population_with_scores, key=lambda x: x[1], reverse=True) 
        
  return population_with_scores_ranked[0]

   