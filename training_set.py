from utils.strategy import *
from utils.save_strat import load_strategy

def getHumanTrainingSet():
    competitors = []
    competitors.append(load_strategy("TFT_strategy.json"))
    competitors.append(load_strategy("STFT_strategy.json"))
    competitors.append(load_strategy("TFTT_strategy.json"))
    competitors.append(load_strategy("AllC_strategy.json"))
    competitors.append(load_strategy("AllD_strategy.json"))
    return competitors