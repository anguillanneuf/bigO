# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:50:13 2018

@author: harrisot

"Given a string of English text and a paragraph width, 
design an algorithm to break the texts into lines not 
exceeding the paragraph width, and not too jagged."
"""

class Lines(object):
  
  def __init__(self, raw="", width=80):
    self.raw = raw
    self.width = width
    self.borders = []
    self.linebreaks = []
    
  def find_borders(self):
    """Find where the cutoffs are"""
    
    for i in range(len(self.raw)):
      if not self.raw[i].isspace():
        if i==0 or self.raw[i-1].isspace():
          self.borders.append(i)
          
        if self.borders and i-self.borders[-1]>self.width:
          print("\"{}\" is longer than the allowed line width {}."
                .format(self.raw[self.borders[-1]:i+1], self.width))
          print("Please consider adjusting the line width.")
          return ''
    self.borders.append(len(self.raw))
    
    
  def break_text_into_lines(self):
    
    self.find_borders()
    lines = ['']
    d = 0
    offset = 0

    for b in self.borders:
      if b-offset < self.width:
        lines[-1] += self.raw[d:b]
      else:
        lines.append(self.raw[d:b])
        offset = d
      d = b
      
    print([len(l) for l in lines])
    return lines
  
  def find_linebreaks(self):
    """
    Select numbers from self.borders such that the difference
    between the neighboring pairs is less than self.width, and
    the sum of squares of all the differences between all 
    neighboring pairs is maximized. 
    
    [0, 4, 10, 16, 18, 25, 28, 36, 41, 45, 47, 57, 64, 71, 
    74, 84, 87, 93, 97, 103, 108, 114, 118, 128, 132, 142,
    149, 153, 157, 161, 168]
    
    """
    print(self.borders)
    return self.linebreaks
  
raw = "Try this: Given a string of English text and a paragraph width, design an algorithm to break the texts into lines not exceeding the paragraph width, and not too jagged."
lines = Lines(raw, 20)
print(lines.break_text_into_lines())
lines.find_linebreaks()