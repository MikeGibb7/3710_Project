# Just to give a visual representation when needed
def moveHistoryNumberToString(num, rounds_played = 3):
  format_value = f'0{str(rounds_played * 2)}b'
  binary = format(num, format_value)
  result = ""

  for bit in binary:
    if bit == '0':
      result += "C"
    else:
      result += "D"

  return result





