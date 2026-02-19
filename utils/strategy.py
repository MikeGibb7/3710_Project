import random
from config import config

def generateRandomStrategy():
  strategy = []

  for x in range(config["rounds_in_memory"]):
    strategy.append(random.choice(['C', 'D']))

  for x in range(2**(config["rounds_in_memory"] * 2)):
    strategy.append(random.choice(['C', 'D']))

  return strategy
  
