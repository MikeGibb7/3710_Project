from config import config

def getHistoryStringFromHistoryNumber(num):
  format_value = f'0{str(config["rounds_in_memory"] * 2)}b'
  binary = format(num - config["rounds_in_memory"], format_value)
  result = ""

  for bit in binary:
    if bit == '0':
      result += "C"
    else:
      result += "D"

  return result

def getHistoryNumberFromHistoryString(num_string):
  binary = ""
  for letter in num_string:
    if letter == "C":
      binary += "0"
    else:
      binary += "1"
  
  value = int(binary, 2)

  return value