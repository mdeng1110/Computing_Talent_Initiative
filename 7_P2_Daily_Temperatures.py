def dailyTemperatures(dailyTemps):
  # create empty list to store days to wait for warmer temperature
  list_of_days = []
  # loop over the entire list to determine how many days for warmer temperature
  for index in range(len(dailyTemps)):
    current_temp = dailyTemps[index]
    count_of_days = 0
    found_it = False
    for check_temp in dailyTemps[index:]:
      if check_temp > current_temp:
      # append to a list of days to wait for warmer temperature
        list_of_days.append(count_of_days)
        found_it = True
        break
      else:
        # increment the count of days
        count_of_days += 1
    if not found_it:
      list_of_days.append(0)
  return list_of_days
  # return list how many days to wait until a warmer temperature
  
	# if there is no future day, return 0
  

sampleInput = [73, 74, 75, 71, 69, 72, 76, 73]
print(dailyTemperatures(sampleInput))