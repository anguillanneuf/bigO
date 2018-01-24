# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 10:57:12 2018

@author: harrisot

Amazon question: Find k nearest points to origin given an array of tuples
"""

# iterative approach
# for each new tuple, calcuate distance
# use a min heap to store the tuple and the distance 
# pop out k items and remove distance 
# Space O(n), Time O(n)

import heapq

def k_nearest_tuples(arr, k):
  myheap = []
  
  for tup in arr:
    dist_metric = tup[0]*tup[0] + tup[1]*tup[1]
    heapq.heappush(myheap, (dist_metric, tup))
    
  output = []

  for v in heapq.nsmallest(k, myheap):
    output.append(v[1])
    
  return output

arr = [(0,1),(-3,1),(2,2),(-1,-2),(0,3),(2,-2)]
print(k_nearest_tuples(arr, 3))