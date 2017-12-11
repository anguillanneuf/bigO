#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:38:27 2017

@author: tz
"""

def circus_tower(pp):
  """O(n*n) time
  O(n) space
  """
  pp = sorted(pp)
  tower = []

  for i in range(len(pp)):
    left = pp[i][1]
    right = max([k[1] for k in pp[i:]])
    temp = []
    
    for j in range(len(pp)):
      if left <= pp[j][1] <= right:
        temp.append(pp[j])
        left = pp[j][1]
        
    if len(temp) > len(tower):
      tower = temp
      
  return tower

pp1 = [(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)]
print(circus_tower(pp1)) 

pp2 = [(75,87),(65,90),(70,91),(71,82),(72,84),(73,85)]
print(circus_tower(pp2)) 

def subsequence_search(arr):
  best = []
  for i in range(len(arr)):
    left = arr[i]
    right = max(arr[i:])
    temp = []
    for j in range(i,len(arr)):
      if left <= arr[j] <= right:
        temp.append(arr[j])
        left = arr[j]
    if len(best)<len(temp):
      best = temp
    
  return best

print(subsequence_search([90,91,81,82,83,74,85])) 