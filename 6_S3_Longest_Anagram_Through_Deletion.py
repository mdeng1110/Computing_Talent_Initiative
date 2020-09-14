string = "batman"
dictionary = ["bat", "aman", "antman"]

def longest_anagram(string, dictionary):
  best = ""
  for d in dictionary:
    temp = ""
    i = 0
    j = 0
    while i < len(d) and j < len(string): 
      if d[i] == string[j]:
        temp += string[j]
        i += 1
        j += 1
      else:
        j += 1
    if len(temp) > len(best):
      best = temp
  return best
print(longest_anagram(string, dictionary))
  


