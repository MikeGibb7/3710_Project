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

score = calculateScoreTournament(first_bot, training_set)

print(f"Score of Robot1: {score}")

## Example of creating a tournament of 50 random strategies and finding the winner

# array_of_strategies = []
# for x in range(50):
#   array_of_strategies.append(generateRandomStrategy())

# max = 0
# winner = 0
# for x in range(len(array_of_strategies)):
#   score = calculateScoreTournament(array_of_strategies[x], array_of_strategies)

#   if max < score:
#     max = score
#     winner = x

# print("Winning strategy: " + str(winner) + " with score " + str(max))
# printStrategy(array_of_strategies[winner])
 