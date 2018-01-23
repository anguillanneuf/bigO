# -*- coding: utf-8 -*-
"""
Created on Tue Jan 16 10:19:00 2018

@author: harrisot
"""

def word_count_engine(document):
  words = document.split()
  output = dict()
  for word in words:
    w = ''
    for ch in word:
      if ch.isalpha():
        w += ch.lower()
        
    if w not in output:
      output.update({w:1})
    else:
      output[w] += 1
      
  output2 = dict()
  
  for word in output:
    if output[word] not in output2:
      output2.update({output[word]: [word]})
    else:
      output2[output[word]].append(word)
  
  output2 = sorted(output2.items(), reverse=True)

  output3=[]
  for key,values in output2:
    for value in sorted(values):
      output3.append([value, str(key)])
  
  return output3

document = "Practice makes perfect. you'll only \
get Perfect by practice. just practice!"

print(word_count_engine(document))