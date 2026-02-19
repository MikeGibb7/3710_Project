from utils.strategy import generateRandomStrategy
from utils.output import printStrategy
from utils.score import calculateScoreTournament

config = {
  "independent_rounds": 3,
  "cooperate_success": 3, 
  "cooperate_failure": 0, 
  "defect_success": 5, 
  "defect_failure": 1,
}

first_bot = generateRandomStrategy(config)
second_bot = generateRandomStrategy(config)

training_set = [
  first_bot,
  second_bot,
]

print("Robot1: ")
printStrategy(first_bot, config)
print("Robot2: ")
printStrategy(second_bot, config)

calculateScoreTournament(first_bot, training_set, config)
 