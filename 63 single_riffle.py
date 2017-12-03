# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:38:00 2017

@author: harrisot
"""

def single_cut_check(cards):
  diffs = set()
  for i,v in enumerate(cards):
    diffs.add(abs(i-v))
  return True if len(diffs) == 2 else False

cards = [i for i in range(33, 53, 1)] + [i for i in range(0, 33)]
#print(single_cut_check(cards))


def single_riffle_check(cards):
  a = None
  b = None
  a_min = None
  b_min = None
  a_max = None
  b_max = None
  
  for i in range(len(cards)):
    
    if i == 0: 
      a = i
      a_min = cards[i]
      continue
    
    if cards[i] - cards[i-1] != 1: 
      if b is None: 
        b = i
        b_min = cards[i]
      
        if b_min > a_min: 
          a_max = b_min - 1
          b_max = max(cards)
        if b_min < a_min:
          b_max = a_min - 1
          a_max = max(cards)
          
      else:
        
        if cards[i] - cards[a] == 1:
          a += 1
        elif cards[i] - cards[b] == 1:
          b += 1
        else:
          return False
        
    else:
      
      if a == i - 1:
        a += 1
      else:
        b += 1
  
  if a_max is None and b_max is None:
    return True
  
  return True

cards1 = [0, 7, 6, 8, 1, 9, 10, 2, 3, 4, 5]
cards2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
cards3 = [0, 1, 2, 3, 4, 6, 5, 7, 8, 9, 10]
print(single_riffle_check(cards1))