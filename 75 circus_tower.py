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
  mem = [[] for _ in range(len(pp))]

  for i in range(len(pp)):
    cond = False
    for j in range(i):
      if pp[i][1] > mem[j][-1][1]:
        cond = True
        mem[i]=mem[j] + [pp[i]]
        tower = max(mem[i], tower, key=len)
    if cond is False:
      mem[i].append(pp[i])

  return tower

pp1 = [(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)]
print(circus_tower(pp1)) 

pp2 = [(75,87),(65,90),(70,91),(71,82),(72,84),(73,85)]
print(circus_tower(pp2)) 

def longest_subsequence(arr):
  mem = [[] for _ in range(len(arr))]
  best = []
  
  for i in range(len(arr)):
    cond = False
    for j in range(i): 
      if arr[i] > mem[j][-1]:
        cond = True
        mem[i] = mem[j] + [arr[i]]
        best = max(mem[i], best, key=len) # key=lambda i: len(i)
    if cond is False:
      mem[i].append(arr[i])
  return best

print(longest_subsequence([80,90,91,81,82,83,74,85]))