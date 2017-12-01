# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:38:00 2017

@author: harrisot
"""

def single_riffle_check(cards):
  diffs = set()
  for i,v in enumerate(cards):
    diffs.add(abs(i-v))
  return True if len(diffs) == 2 else False

cards = [i for i in range(33, 53, 1)] + [i for i in range(0, 33)]
cards = [i for i in range(1, 53, 1)] + [0] + [9]
print(single_riffle_check(cards))