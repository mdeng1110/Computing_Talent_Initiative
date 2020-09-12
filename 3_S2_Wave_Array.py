def wave_array(integers):
  # y, x = x, y
  #print("LENGTH: ", len(integers))
  integers.sort()
  
  for i in range(1, len(integers)):
    if i % 2 == 1:
      if integers[i - 1] <= integers[i]:
        integers[i - 1], integers[i] = integers[i], integers[i - 1]
    else:
        if integers[i - 1] >= integers[i]:
          integers[i - 1], integers[i] = integers[i], integers[i - 1]
  return integers
  
print(wave_array([1, 2, 3, 4]))