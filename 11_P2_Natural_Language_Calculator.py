def nlp_calculator(statement):
  parts = statement.split()
  converted_parts = []
  for part in parts:
    if part == "and" or part == "from" or part == "by":
      continue
    if translator.get(part):
      converted_parts.append(translator.get(part))
    else:
      converted_parts.append(word_to_number(part))
  if "from" in parts:
    return (number_to_word(converted_parts[0](converted_parts[2], converted_parts[1])))
  return (number_to_word(converted_parts[0](converted_parts[1], converted_parts[2])))

def word_to_number(word):
  result = [words[ele] for ele in word.split('-')]
  return sum(result)

  
def number_to_word(num):
  word = numbers.get(num, False)
  if word:
    return word
  tens = (num // 10) * 10
  ones = num % 10
  if num < 0:
    return "negative " + str(numbers.get(abs(num)))
  return str(numbers.get(tens)) + "-" + str(numbers.get(ones))
  
def add(a,b):
  return a + b
  
def subtract(a,b):
  return a - b

def multiply(a,b):
  return a * b
  
def divide(a,b):
  return int(a / b)
  
numbers = {
  1 : "one",
  2 : "two",
  3 : "three",
  4 : "four",
  5 : "five",
  6 : "six",
  7 : "seven",
  8 : "eight",
  9 : "nine",
  10 : "ten",
  11 : "eleven",
  12 : "twelve",
  13 : "thirteen",
  14 : "fourteen",
  15 : "fifteen",
  16 : "sixteen",
  17 : "seventeen",
  18 : "eighteen",
  19 : "nineteen",
  20 : "twenty",
  30 : "thirty",
  40 : "forty",
  50 : "fifty",
  60 : "sixty",
  70 : "seventy",
  80 : "eighty",
  90 : "ninety",
  100: "hundred"
}
  
words = {
  "one" : 1,
  "two" : 2,
  "three" : 3,
  "four" : 4,
  "five" : 5,
  "six" : 6,
  "seven" : 7,
  "eight" : 8,
  "nine" : 9,
  "ten" : 10,
  "eleven" : 11,
  "twelve" : 12,
  "thirteen" : 13,
  "fourteen" : 14,
  "fifteen" : 15,
  "sixteen" : 16,
  "seventeen" : 17,
  "eighteen" : 18,
  "nineteen" : 19,
  "twenty" : 20,
  "thirty" : 30,
  "forty" : 40,
  "fifty" : 50,
  "sixty" : 60,
  "seventy" : 70,
  "eighty" : 80,
  "ninety" : 90,
  "hundred" : 100
}
  
translator = {
  "add": add,
  "subtract": subtract,
  "multiply": multiply,
  "divide": divide
}

#print(translator["subtract"](14,2))
# print(number_to_word(99))
#print(word_to_number("twenty-two"))
print(nlp_calculator('subtract ten from two'))