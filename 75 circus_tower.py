#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:38:27 2017

@author: tz
"""

def circus_tower(pp):
  """O(nlogn)+O(n) time
  O(n) space
  Maybe if I use a black red tree or an AVL tree, I can
  reduce it down to O(n) time to create tree and O(n)
  time to traverse the tree to create the output
  """
  pp = sorted(pp) # do I need to write this?
  tower = []

  for i,v in enumerate(pp):
    if i == 0: 
      tower.append(pp[i])
      continue
    if v[1] > tower[-1][1]:
      tower.append(pp[i])
  return tower

pp1 = [(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)]
print(circus_tower(pp1))

pp1 = [(75,87),(65,90),(70,91),(71,82),(72,84),(73,85),(74,86)]
print(circus_tower(pp1))

# how to search for sub sequences in an array in O(n^2) and O(nlogn) time