import random

def getHistoryStringFromHistoryNumber(num, rounds_played = 3):
  format_value = f'0{str(rounds_played * 2)}b'
  binary = format(num - rounds_played, format_value)
  result = ""

  for bit in binary:
    if bit == '0':
      result += "C"
    else:
      result += "D"

  return result

def getHistoryNumberFromHistoryString(num_string):
  binary = ""
  for letter in num_string:
    if letter == "C":
      binary += "0"
    else:
      binary += "1"
  
  value = int(binary, 2)

  return value

def printStrategy(strategy, rounds_played):
  for x in range(rounds_played):
    print(f"Move {x}: {strategy[x]}")

  print("Next move strategy:")
  for x in range(rounds_played, len(strategy)):
    print(f"{getHistoryStringFromHistoryNumber(x, rounds_played)}: {strategy[x]}")  

def generateRandomStrategy(rounds_played = 3):
  strategy = []

  for x in range(rounds_played):
    strategy.append(random.choice(['C', 'D']))

  for x in range(2**(rounds_played * 2)):
    strategy.append(random.choice(['C', 'D']))

  return strategy
  
def calculateScore(strategy_a, strategy_b, cooperateSuccess, cooperateFailure, defectSuccess, defectFailure, rounds_played = 3): 
  scoreA = 0
  scoreB = 0
  historyA = "";
  historyB = "";
  for x in range(rounds_played):
    moveA = strategy_a[x]
    moveB = strategy_b[x]

    historyA += moveA + moveB
    historyB += moveB + moveA

    scoreA += calculateMove(strategy_a[x], strategy_b[x], cooperateSuccess, cooperateFailure, defectSuccess, defectFailure)
    scoreB += calculateMove(strategy_b[x], strategy_a[x], cooperateSuccess, cooperateFailure, defectSuccess, defectFailure)

  print("First 3 rounds: ")
  print(f"FirstBot: {scoreA}, SecondBot: {scoreB}")
  print(f"HistoryA = \"{historyA}\", HistoryB = \"{historyB}\"")

  strategy_a_index = getHistoryNumberFromHistoryString(historyA) + rounds_played
  strategy_b_index = getHistoryNumberFromHistoryString(historyB) + rounds_played

  scoreA += calculateMove(strategy_a[strategy_a_index], strategy_b[strategy_b_index], cooperateSuccess, cooperateFailure, defectSuccess, defectFailure)
  scoreB += calculateMove(strategy_b[strategy_b_index], strategy_a[strategy_a_index], cooperateSuccess, cooperateFailure, defectSuccess, defectFailure)

  print(f"Final Score: ")
  print(f"FirstBot: {scoreA}, SecondBot: {scoreB}")
    
def calculateMove(moveA, moveB, cooperateSuccess, cooperateFailure, defectSuccess, defectFailure):
  if moveA == 'C' and moveB == 'C':
    return cooperateSuccess
  elif moveA == 'C' and moveB == 'D':
    return cooperateFailure
  elif moveA == 'D' and moveB == 'C':
    return defectSuccess
  elif moveA == 'D' and moveB == 'D':
    return defectFailure