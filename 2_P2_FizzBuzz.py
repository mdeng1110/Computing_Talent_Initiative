def fizzbuzz(n):
    for fizzbuzz in range(1,n + 1):
      if fizzbuzz % 3 == 0 and fizzbuzz % 5 == 0:
        print("fizzbuzz")
        continue
      elif fizzbuzz % 3 == 0:
        print("fizz")
        continue
      elif fizzbuzz % 5 == 0:
        print("buzz")
        continue
      print(fizzbuzz)

# Please do not modify the code below this line.
# When you run your code, you will need to enter 
# an input in the terminal below, where the prompt appears

test_case = int(input("Please enter an input number:"))
fizzbuzz(test_case)