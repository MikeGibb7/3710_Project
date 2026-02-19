from utils.convert import getHistoryStringFromHistoryNumber
from config import config

def printStrategy(strategy):
  for x in range(config["rounds_in_memory"]):
    print(f"Move {x}: {strategy[x]}")

  print("Next move strategy:")
  for x in range(config["rounds_in_memory"], len(strategy)):
    print(f"{getHistoryStringFromHistoryNumber(x)}: {strategy[x]}")  

  print()
