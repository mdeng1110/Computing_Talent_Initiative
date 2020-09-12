def roman_to_decimal(roman_numeral):
  roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
  i = 0
  total = 0
  current_character = 0
  next_character = 0
  if len(roman_numeral) == 1:
    return roman[roman_numeral]
  for i in range(len(roman_numeral)):
    if i + 1 < len(roman_numeral):
      current_character = roman[roman_numeral[i]]
      next_character = roman[roman_numeral[i + 1]]
      if current_character < next_character:
        total += (next_character - current_character)
      else:
        total += (current_character + next_character)
        i += 1
    else:
      total += (current_character + next_character)
      i += 1
    return total
#roman_numeral = input()
#print(roman_to_decimal(roman_numeral))      


