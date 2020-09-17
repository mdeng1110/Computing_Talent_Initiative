import re
def count_words(text):
  # split the text into words
  words = text.split()
  dictionary = {}
  result = ""
  # loop over each word
  for i in range(len(words)):
      # lower case the word, strip the punctuation
      words[i] = words[i].lower()
      words[i] = re.sub(r'[.,~?!\s]', '', words[i]) 
      # if word exists in the dict, count up
      if words[i] in dictionary:
        dictionary[words[i]] += 1
      # otherwise: add the word to the dict
      else:
        dictionary[words[i]] = 1
  # loop over every key on the dict and print the key and value
  for key, value in dictionary.items():
    result += '{WORD} {COUNT}\n'.format(WORD=key, 
                                        COUNT=value)
  # return that string
  return result
text = "I do not like green eggs and ham, I do not like them, Sam-I-Am"
print(count_words(text))