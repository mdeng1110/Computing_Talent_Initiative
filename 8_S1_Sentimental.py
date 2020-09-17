import re
def sentiment_scores(sentiments, texts):
  # get rid of the punctuation
  output = []
  # for loop of texts
  for i in range(len(texts)):
    value = 0
    # strip of the puncation from the sentence
    sentence = texts[i]
    sentence = re.sub(r'[^\w\s]','',sentence)
    sentence = sentence.split()
    for j in range(len(sentence)):
      if(sentence[j] in sentiments):
        value = value + sentiments[sentence[j]]
        
    output.append(value)
  return output
# use split(), isalnum(), replace(two parameters= "!", "")
# "that makes me so happy! amazing."
                    #0.8    #0.4 = 1.2
sentiments = {
 "amazing": 0.4,
 "sad": -0.8,
 "great": 0.8,
 "no": -0.1,
 "yes": 0.1,
 "angry": -0.7,
 "happy": 0.8
}

texts = [
  "that makes me so happy! amazing.", 
  "I'm so angry about this sad thing.", 
  "sad but true, amazing",
  "yes that is great, and amazing"
]
