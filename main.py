from strategyFunctions import calculateScore, generateRandomStrategy, printStrategy

rounds_played = 3

firstBot = generateRandomStrategy(rounds_played)
secondBot = generateRandomStrategy(rounds_played)
print("Robot1: ")
printStrategy(firstBot, rounds_played)
print()
print("Robot2: ")
printStrategy(secondBot, rounds_played)
print()
print("Battle")
calculateScore(firstBot, secondBot, 3, 0, 5, 1, rounds_played)
 