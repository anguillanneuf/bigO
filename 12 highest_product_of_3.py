#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  3 16:47:49 2017

@author: tz
"""
import heapq
from functools import reduce

def highest_product_of_3(ints):
  if len(ints) <3:
    return "Not enough values!"
  
  neg=[]
  pos=[]
  
  heapq.heapify(neg)
  heapq.heapify(pos)
  
  for i in ints:
    if i >= 0:
      heapq.heappush(pos,i)
      if len(pos) > 3:
        heapq.heappop(pos)
    else:
      heapq.heappush(neg, i)
  
  if len(neg)<=1:
    return reduce(lambda a,b: a*b, pos)

  heapq.nsmallest(2,neg)

  n1n2 = neg[0]*neg[1]
  
  if len(pos)==0:
    temp = heapq.nlargest(3,neg)
    return reduce(lambda a,b: a*b, temp)
  elif len(pos)==1:
    p1 = heapq.heappop(pos)
    return n1n2*p1
  elif len(pos)==2:
    p = heapq.heappop(pos)
    p = heapq.heappop(pos)
    return n1n2*p
  else:
    p1 = heapq.heappop(pos)
    p2 = heapq.heappop(pos)
    p3 = heapq.heappop(pos)
    return max(p3*p2*p1, n1n2*p3)
    

ints = [-1, -9, 2,4,6] #[2,4,6,0,9,3,6]
print(highest_product_of_3(ints))

#==============================================================================
# Reflection:
# Why doesn't my solution look elegant? How could I have done better?
# Perhaps I could have considered making `pos` and `neg` of length 2.
# Instead of keeping a list, keep a running product.
# Instead of thinking in terms of pos/neg, perhaps lowest/highest works.
#==============================================================================
