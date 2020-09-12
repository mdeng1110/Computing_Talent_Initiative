#integers = input()
#integers = integers.split()

def single_number(integers):
  #for loop and count how many times integer occurred
  result = int(integers[0])
  for i in range(1, len(integers)):
    result = result ^ int(integers[i])
  return result
  
#print(single_number(integers))