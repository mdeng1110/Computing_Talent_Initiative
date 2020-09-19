def hammingDistance(x, y):
	distance = 0
	for i in range(31, -1, -1):
	   a = x >> i & 1
	   b = y >> i & 1
	   if not(a == b):
	     distance += 1
	   #x = x >> 1
	return distance
testX = 1
testY = 4
testResult = hammingDistance(testX, testY)
print(testResult)