#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 20:39:55 2018

@author: tz
"""
def couples_holding_hands(row):
  swap = 0
  pairs = []
  
  for p in range(len(row)//2):
    p1 = row[p*2]//2
    p2 = row[p*2+1]//2
    if p1!=p2:
      pairs.append(sorted([row[p*2]//2, row[p*2+1]//2]))
      
  pairs = sorted(pairs)
  
  while len(pairs)>1:

    pp1 = pairs.pop(0)
    pp2 = pairs.pop(0)
    
    if pp1[0]==pp2[0]:
      swap += 1
      if pp1[1]!=pp2[1]:
        pairs.append(sorted([pp1[1], pp2[1]]))
        pairs = sorted(pairs)
        
  return swap
  
print(couples_holding_hands_2([1,4,0,5,8,7,6,3,2,9]))