from utils.convert import getHistoryNumberFromHistoryString
from config import config

def calculateScore(strategy_a, strategy_b): 
  score_a = 0
  score_b = 0
  history_a = "";
  history_b = "";

  # First few rounds independant of other player
  for x in range(config["rounds_in_memory"]):
    move_a = strategy_a[x]
    move_b = strategy_b[x]

    history_a += move_a + move_b
    history_b += move_b + move_a

    move_score_a, move_score_b = calculateMove(strategy_a[x], strategy_b[x])
    score_a += move_score_a
    score_b += move_score_b

  print("First 3 rounds: ")
  print(f"FirstBot: {score_a}, SecondBot: {score_b}")

  # Rounds that rely on previous move context
  for x in range(config["total_rounds"] - config["rounds_in_memory"]):
    print(f"Round {1 + x + config['rounds_in_memory']}: history_a = \"{history_a}\", history_b = \"{history_b}\"")

    strategy_a_index = getHistoryNumberFromHistoryString(history_a) + config["rounds_in_memory"]
    strategy_b_index = getHistoryNumberFromHistoryString(history_b) + config["rounds_in_memory"]

    move_a = strategy_a[strategy_a_index]
    move_b = strategy_b[strategy_b_index]

    history_a = history_a[2:] + move_a + move_b
    history_b = history_b[2:] + move_b + move_a

    move_score_a, move_score_b = calculateMove(move_a, move_b)
    score_a += move_score_a
    score_b += move_score_b

  print(f"Final Score: ")
  print(f"FirstBot: {score_a}, SecondBot: {score_b}")
  print()

  return score_a, score_b
    
def calculateMove(move_a, move_b):
  if move_a == 'C' and move_b == 'C':
    return config["cooperate_success"], config["cooperate_success"]
  elif move_a == 'C' and move_b == 'D':
    return config["cooperate_failure"], config["defect_success"]
  elif move_a == 'D' and move_b == 'C':
    return config["defect_success"], config["cooperate_failure"]
  elif move_a == 'D' and move_b == 'D':
    return config["defect_failure"], config["defect_failure"]
  
def calculateScoreTournament(strategy, training_set):
  score = 0
  for competitor in training_set:
    scoreA, _ = calculateScore(strategy, competitor)
    score += scoreA

  # print(f"Cumulative score of strategy: {score}")

  return score