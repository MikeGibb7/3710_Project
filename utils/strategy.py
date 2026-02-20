import random
from config import config
from utils.convert import getHistoryNumberFromHistoryString, getHistoryStringFromHistoryNumber

class Strategy:
  def __init__(self, strategy, rounds_in_memory):
    self.move_list = strategy
    self.rounds_in_memory = rounds_in_memory

  def getMove(self, history):
    # This logic will activate the first few moves that are independant of the other player
    if int(len(history) / 2) < self.rounds_in_memory:
      return self.move_list[int(len(history) / 2)]
    
    # This logic will activate the moves that rely on the previous move context
    move_index = getHistoryNumberFromHistoryString(history) + self.rounds_in_memory
    return self.move_list[move_index]
  
  def printStrategy(self):
    for x in range(self.rounds_in_memory):
      print(f"Move {x}: {self.move_list[x]}")

    print("Next move strategy:")
    for x in range(self.rounds_in_memory, len(self.move_list)):
      print(f"{getHistoryStringFromHistoryNumber(x, self.rounds_in_memory)}: {self.move_list[x]}")  

    print()

def generateRandomStrategy(rounds_in_memory):
  move_list = []

  for x in range(rounds_in_memory):
    move_list.append(random.choice(['C', 'D']))

  for x in range(2**(rounds_in_memory * 2)):
    move_list.append(random.choice(['C', 'D']))

  return Strategy(move_list, rounds_in_memory)
