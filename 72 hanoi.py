#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 16:16:00 2017

@author: tz
"""

def hanoi(n, loc, temp, dest):
  if n == 0:
    return
  
  hanoi(n-1, loc, dest, temp)
  
  piece = loc.pop()
  dest.append(piece)
  
  hanoi(n-1, temp, loc, dest)
  
n = 3
loc = [3,2,1]
temp = []
dest = []
hanoi(n, loc, temp, dest)
print(loc, temp, dest)