from utils.convert import getHistoryStringFromHistoryNumber
from config import config

def printStrategy(strategy):
  for x in range(config["independent_rounds"]):
    print(f"Move {x}: {strategy[x]}")

  print("Next move strategy:")
  for x in range(config["independent_rounds"], len(strategy)):
    print(f"{getHistoryStringFromHistoryNumber(x)}: {strategy[x]}")  

  print()
