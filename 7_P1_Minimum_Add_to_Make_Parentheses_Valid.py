def minAddToMakeValid(S):
	removed = True
	while removed:
	  removed = False
	  input_string_length = len(S)
	  S = S.replace("()", "")
	  if len(S) < input_string_length:
	    removed = True
	return len(S)
sampleInput = '())'
print(minAddToMakeValid(sampleInput))
