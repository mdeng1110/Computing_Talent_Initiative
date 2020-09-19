def find_center(matrix):
  sum_of_x = 0
  sum_of_y = 0
  total_outbreaks = 0
  
  for key, outbreaks in matrix.items():
    x = int(key.split(",")[0])
    y = int(key.split(",")[1])
    
    sum_of_x += (x * outbreaks)
    sum_of_y += (y * outbreaks)
    
    total_outbreaks += outbreaks
  avg_x = round(sum_of_x / total_outbreaks)
  avg_y = round(sum_of_y / total_outbreaks)
  return str(avg_x) + "," + str(avg_y)
# input is a dictionary
# remember to round the number
# output is a string(coordinate)

reported_outbreak = {
  "5,5": 10,
  "5,6": 8,
  "5,4": 8,
  "4,5": 8,
  "4,5": 8,
  "4,6": 8,
  "6,6": 7,
  "6,5": 8,
  "4,4": 8,
  "3,4": 4,
  "3,3": 2,
  "6,7": 2
}

print(find_center(reported_outbreak))