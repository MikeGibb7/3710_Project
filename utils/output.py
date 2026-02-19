from utils.convert import getHistoryStringFromHistoryNumber

def printStrategy(strategy, config):
  for x in range(config["independent_rounds"]):
    print(f"Move {x}: {strategy[x]}")

  print("Next move strategy:")
  for x in range(config["independent_rounds"], len(strategy)):
    print(f"{getHistoryStringFromHistoryNumber(x, config)}: {strategy[x]}")  

  print()
