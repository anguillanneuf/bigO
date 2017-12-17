#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 17:39:14 2017

@author: tz
"""

def sets_from_set(S):

  ans = [set()]
  
  while len(S)>0:
    curr = S.pop()
    temp=[]
    for item in ans:   
      temp.append(item.union(curr))
    ans.extend(temp)
  return ans

S = {'a','b','c'}
print(sets_from_set(S))