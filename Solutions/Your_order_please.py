def order(sentence):
  s = sentence.split(" ")
  res = ""
  for i in range(len(s)):
        for w in s:
            if w.__contains__(str(i + 1)):
                res += w + " "
  
  return res[:len(sentence)]
