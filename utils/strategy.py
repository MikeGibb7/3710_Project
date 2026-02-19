import random

def generateRandomStrategy(config):
  strategy = []

  for x in range(config["independent_rounds"]):
    strategy.append(random.choice(['C', 'D']))

  for x in range(2**(config["independent_rounds"] * 2)):
    strategy.append(random.choice(['C', 'D']))

  return strategy
  
