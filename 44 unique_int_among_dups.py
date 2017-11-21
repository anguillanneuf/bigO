# -*- coding: utf-8 -*-
"""
Created on Mon Nov 20 17:15:56 2017

@author: harrisot
"""

def find_unique_among_dups(ints):
  """Time: O(N) 
  Space: O(N)
  """
  uniques = dict()
  for i in ints:
    if i not in uniques.keys():
      uniques.update({i: 1})
    else:
      uniques.pop(i)
  if len(uniques)==0:
    return None
  return list(uniques.keys())[0]



def find_unique_among_dups_fast(ints):
  """Magic!!!"""
  temp = 0
  for i in ints: 
    temp ^= i
  return temp

ints = [12,4,90,8,12,7,7,8,49,4,90]
print(find_unique_among_dups(ints))
print(find_unique_among_dups_fast(ints))