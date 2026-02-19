from utils.convert import getHistoryNumberFromHistoryString
from config import config

def calculateScore(strategy_a, strategy_b): 
  score_a = 0
  score_b = 0
  history_a = "";
  history_b = "";

  # First few rounds independant of other player
  for x in range(config["independent_rounds"]):
    move_a = strategy_a[x]
    move_b = strategy_b[x]

    history_a += move_a + move_b
    history_b += move_b + move_a

    move_score_a, move_score_b = calculateMove(strategy_a[x], strategy_b[x])
    score_a += move_score_a
    score_b += move_score_b

  print("First 3 rounds: ")
  print(f"FirstBot: {score_a}, SecondBot: {score_b}")
  print(f"HistoryA = \"{history_a}\", HistoryB = \"{history_b}\"")

  # Rounds that rely on previous move context
  strategy_a_index = getHistoryNumberFromHistoryString(history_a) + config["independent_rounds"]
  strategy_b_index = getHistoryNumberFromHistoryString(history_b) + config["independent_rounds"]

  move_score_a, move_score_b = calculateMove(strategy_a[strategy_a_index], strategy_b[strategy_b_index])
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

  print(f"Cumulative score of strategy: {score}")

  return score