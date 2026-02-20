from utils.convert import getHistoryNumberFromHistoryString
from config import config

def calculateScore(strategy_a, strategy_b): 
  score_a = 0
  score_b = 0
  history_a = "";
  history_b = "";

  for x in range(config["total_rounds"]):
    # print(f"Round {x}: ")
    # print(f"History of Robot1: {history_a}, History of Robot2: {history_b}")
    
    move_a = strategy_a.getMove(history_a)
    move_b = strategy_b.getMove(history_b)

    history_a += move_a + move_b
    history_a = history_a[-(strategy_a.rounds_in_memory * 2):]
    history_b += move_b + move_a
    history_b = history_b[-(strategy_b.rounds_in_memory * 2):]

    move_score_a, move_score_b = calculateMove(move_a, move_b)
    score_a += move_score_a
    score_b += move_score_b

    # print(f"Robot1: {move_a}, Robot2: {move_b}")
    # print(f"Score of Robot1: {score_a}, Score of Robot2: {score_b}")
    # print()

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

  return score