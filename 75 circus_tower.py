#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 21:38:27 2017

@author: tz
"""

def circus_tower(pp):
  pp = sorted(pp)
  tower = []

  for i,v in enumerate(pp):
    if i == 0: 
      tower.append(pp[i])
      continue
    if v[1] > pp[i-1][1]:
      tower.append(pp[i])
  return tower


pp1 = [(65,100),(70,150),(56,90),(75,190),(60,95),(68,110)]
print(circus_tower(pp1))

pp1 = [(75,100),(65,90),(70,89)]
print(circus_tower(pp1))