#words = input()
#print("words: ", len(words))
def length_of_last_word(words):
  if " " in words:
    last_word = words.rsplit(' ',1)[1]
    return len(last_word)
  else:
    return len(words)
# print(length_of_last_word(words))
# print(length_of_last_word("Hello World"))
# print(length_of_last_word("aaa bbb aaaa"))
#print(length_of_last_word("aaa"))