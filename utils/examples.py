from utils.strategy import Strategy, generateRandomStrategy
from utils.score import calculateScoreTournament, humanVsRobot
import random

first_bot = generateRandomStrategy(3)
second_bot = generateRandomStrategy(2)
tit_for_tat = Strategy(['C', 
                        'C', 'D', 'C', 'D'], 1)
tit_for_two_tat = Strategy(['C', 'C', 
                            'C', 'C', 'C', 'C', 'C', 'D', 'C', 'D', 'C', 'C', 'C', 'C', 'C', 'D', 'C', 'D'], 2)
suspicious_tit_for_tat = Strategy(['D', 
                        'C', 'D', 'C', 'D'], 1)

def simpleExampleRobotsFighting():
  training_set = [
    first_bot,
    second_bot,
  ]

  print("Robot1: ")
  first_bot.printStrategy()
  print("Robot2: ")
  second_bot.printStrategy()

  score = calculateScoreTournament(first_bot, training_set)

  print(f"Score of Robot1: {score}")
 
def playARobotExample():
  score_human, score_robot = humanVsRobot(suspicious_tit_for_tat)
  print(f"Score of Human: {score_human}, Score of Robot: {score_robot}")

def tournamentOf50RandomStrategiesExample():
  array_of_strategies = []
  for x in range(50):
    array_of_strategies.append(generateRandomStrategy(random.choice([1, 2, 3])))

  max = 0
  winner = 0
  for x in range(len(array_of_strategies)):
    score = calculateScoreTournament(array_of_strategies[x], array_of_strategies)

    if max < score:
      max = score
      winner = x

  print("Winning strategy: " + str(winner) + " with score " + str(max))
  array_of_strategies[winner].printStrategy()