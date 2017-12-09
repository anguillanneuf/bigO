#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 16:54:31 2017

@author: tz
"""

def child_steps(tot, steps):
  """This is like combinations, not permutations
  This is a bottom up approach, which I prefer!"""
  mem = [0]*(tot+1)
  
  for step in sorted(steps):
    
    temp = step
    mem[temp] = mem[temp] + 1
    while temp <= tot:
      mem[temp] += mem[temp-step]
      temp += 1

  return mem[tot]

print("My solution: {} combinations to make 100".format(child_steps(100,[1,2,3])))



def helper(amt, denoms, i, cm, cm2):
  """This is a top-down approach"""

  if i >= len(denoms)-1:
    cm2[amt][i] = 1
    return 1
  
  if cm2[amt][i] > 0: 
    return cm2[amt][i]
  
  if cm[amt] > 0: 
    return cm[amt]

  ways = 0
  
  for x in range(0, amt+1, denoms[i]):
    ways += helper(amt-x, denoms, i+1,cm,cm2)
    
  cm[amt] = ways
  cm2[amt][i] = ways
  
  return ways

def makeChange(amt, denoms):
  """[0,0,0]*n creates n references to [0,0,0]
  However, [[0,0,0] for _ in range(n)] creates n lists"""
  
  cm = [0 for _ in range(amt+1)]
  cm2 = [[0 for _ in range(len(denoms))] for _ in range(amt+1)]
  
  return helper(amt, denoms, 0, cm, cm2)

print("My bottom-up solution: {}".format(child_steps(25,[1,5,10,25])))
print("Book solution: {}".format(makeChange(25,(25,10,5,1))))


mem = [-1] * 101
def child_steps_new(tot = 100):
  """This is like permutations, not combinations"""
  if tot < 0:
    return 0 
  elif tot == 0:
    return 1
  elif mem[tot] > -1:
    return mem[tot]
  else:
    mem[tot] = child_steps_new(tot-1) + child_steps_new(tot-2) + child_steps_new(tot-3)
    return mem[tot]

print("Book solution: {} permutations to make 100".format(child_steps_new(100)))

def coin_representations(n, denom_index=0, denoms=(1, 5, 10, 25)):
    if n == 0:  # base case: we've found a combination of coins that divides evenly into amount of change
        return 1
    if denom_index >= len(denoms):  # check for case where we don't ever pick any coins
        return 0
    coin = denoms[denom_index]  # current coin we pick. we only pick one type of coin at each recursion level
    branches = n // coin  # max number of times we can pick this coin.
    representations = 0
    while branches >= 0:  # subtract coin value from n for each recursive call. there is one case where we pick 0 coins!
        representations += coin_representations(n - branches*coin, denom_index + 1, denoms)
        branches -= 1
    return representations
  
  
print("Classmate solution: {}".format(coin_representations(25,0,(1,5,10,25))))