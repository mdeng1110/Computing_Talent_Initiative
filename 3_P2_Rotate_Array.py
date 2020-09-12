# array and k are the inputs
#input_array = list(input())
#k = int(input())
def rotate_array(input_array, k):
  # slice the array based on k
  #(starting position and end position)
  # add the end slice to the beginning 
  # of the array
  if k < len(input_array):
    input_array[:] = input_array[-k:] + input_array[0:-k]
  #return input_array
  
#print(rotate_array(input_array, k))
  
  