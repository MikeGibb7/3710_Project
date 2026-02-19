from utils.strategy import generateRandomStrategy
from utils.output import printStrategy
from utils.score import calculateScoreTournament

first_bot = generateRandomStrategy()
second_bot = generateRandomStrategy()

training_set = [
  first_bot,
  second_bot,
]

print("Robot1: ")
printStrategy(first_bot)
print("Robot2: ")
printStrategy(second_bot)

calculateScoreTournament(first_bot, training_set)
 