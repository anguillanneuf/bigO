# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:50:13 2018

@author: harrisot

"Given a string of English text and a paragraph width, 
design an algorithm to break the texts into lines not exceeding the paragraph width,
 and not too jagged."
"""

class Lines(object):
  
  def __init__(self, raw="", width=80):
    self.raw = raw
    self.width = width
    
  def break_text_into_lines(self):
    
    word_beginnings = []
    
    for i in range(len(self.raw)):
      
      if not self.raw[i].isspace():
        
        if i==0 or self.raw[i-1].isspace():
          word_beginnings.append(i)
          
        if word_beginnings and i-word_beginnings[-1]>self.width:
          print(word_beginnings, i)
          print("\"{}\" is longer than the allowed line width {}".format(self.raw[word_beginnings[-1]:i+1], self.width))
          print("Please adjust the line width and try again!")
          return
      
    lines = ['']
    d = 0
    offset = 0
#    print(word_beginnings)
    for b in word_beginnings+[len(self.raw)]:
      if b-offset < self.width:
        lines[-1] += self.raw[d:b]
      else:
        lines.append(self.raw[d:b])
        offset = d
      d = b
      
    print([len(l) for l in lines])
    return lines
  
raw = "Try this: Given a string of English text and a paragraph width, design an algorithm to break the texts into lines not exceeding the paragraph width, and not too jagged."
indent = Lines(raw, 20)
print(indent.break_text_into_lines())

  
  
  

    

