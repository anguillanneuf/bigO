# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 13:50:13 2018

@author: harrisot

"Given a string of English text and a paragraph width, 
design an algorithm to break the texts into lines not 
exceeding the paragraph width, and not too jagged."
"""

from itertools import product

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
          self.borders = []
          
    self.borders.append(len(self.raw))
    
    
  def break_text_into_lines(self):
    """Naive implementation"""
    
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

  def find_next_linebreak(self, p, reversed=False):
    """
    Given the starting index of a line, find the starting index of the
    next line such that this line is being filled as much as possible
    """
    
    if not reversed:
      if p == len(self.borders)-1: return None
      i = p
      j = len(self.borders)-1
      if self.borders[j] - self.borders[i] <= self.width: return j
      sign = 1
    else:
      if p == 0: return None
      i = 0
      j = p
      if self.borders[j] - self.borders[i] <= self.width: return i
      sign = -1
      
    while i < j:
      m = (i+j)//2
      if self.borders[m-1] <= self.borders[p]+sign*self.width <= self.borders[m]:
        p = m-1*(not reversed)
        break
      elif self.borders[m] > self.borders[p]+sign*self.width:
        j = m
      else:
        i = m

    return p
  
  def find_linebreaks(self):
    """
    Select numbers from self.borders such that the difference
    between the neighboring pairs is less than self.width, and
    the sum of squares of all the differences between all 
    neighboring pairs is minimized.     
    """
    self.find_borders()
    
    # Try to squeeze as much as possible from front to back
    front_push = []
    p = 0

    while p is not None and p <= len(self.borders):
      front_push.append((p, self.borders[p]))
      p = self.find_next_linebreak(p)
    
    print("front push results: ", front_push)
    
    # Try to squeeze as much as possible from back to front
    back_push = []
    p = len(self.borders)-1

    while p is not None and p >= 0: 
      back_push.append((p, self.borders[p]))
      p = self.find_next_linebreak(p, reversed=True)
    
    print("back push results: ", back_push[::-1])
    
    # Brute force search
    min_cost = float('inf')
    possible_ranges = []
    
    for back,front in zip(back_push[::-1], front_push):
      possible_ranges.append(range(back[0], front[0]+1))

    print("Possible ranges: ", possible_ranges)
    for scenario in product(*possible_ranges):

      cost = 0
      for k in range(1,len(scenario)):
        cost += (self.width - (self.borders[scenario[k]]-self.borders[scenario[k-1]]))**2
        
      if cost < min_cost:
        min_cost = cost
        self.linebreaks = [self.borders[k] for k in scenario]
  



raw = "Try this: Given a string of English text and a paragraph width, design an algorithm to break the texts into lines not exceeding the paragraph width, and not too jagged."
lines = Lines(raw, 30)
lines.find_linebreaks()

for b in range(1,len(lines.linebreaks)):
  print(raw[lines.linebreaks[b-1]:lines.linebreaks[b]])