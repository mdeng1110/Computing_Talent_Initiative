def lengthOfLastWord(string):
	if " " in string:
	  word = string.split(" ")[-1]
	  return len(word)
	else:
	  return 0
sampleInput = "Hello World"
print(lengthOfLastWord(sampleInput))
