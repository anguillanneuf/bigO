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

cards1 = [6, 7, 0, 8, 1, 9, 10, 2, 3, 4, 5] # True
cards2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # True
cards3 = [0, 1, 2, 3, 4, 6, 5, 7, 8, 9, 10] # True
print(single_riffle_check(cards1))
print(single_riffle_check(cards2))
print(single_riffle_check(cards3))


def is_single_riffle(arr1, arr2, shuffled_deck):
  """Input: arr1, arr2, shuffled_deck"""
  a1 = b1 = 0
  a2 = len(arr1)-1
  b2 = len(arr2)-1
  
  for card in shuffled_deck:
    if a1 <= a2 and card == arr1[a1]:
      a1 += 1
      
    elif b1 <= b2 and card == arr2[b1]:
      b1 += 1
      
    else:
      return False
    
  return True
  

print(is_single_riffle([6,7,8,9,10],[0,1,2,3,4,5],cards1))
print(is_single_riffle([6,7,8,9,10],[0,1,2,3,4,5],cards2))
print(is_single_riffle([6,7,8,9,10],[0,1,2,3,4,5],cards3))