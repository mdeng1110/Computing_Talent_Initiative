def excel_column_to_number(column):
  number = 0
  if len(column) == 3:
    number = ((ord(column[0]) - 64) * 26 ** 2) + ((ord(column[1]) - 64) * 26) + (ord(column[2]) - 64)
  elif len(column) == 2:
    number = ((ord(column[0]) - 64) * 26) + (ord(column[1]) - 64)
  else:
    number = ord(column[-1]) - 64
  return number
  
  
print(excel_column_to_number('AB'))
