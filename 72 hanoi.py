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
  
  loc_temp = loc
  dest_temp = dest
  piece = loc[0].pop()
  dest[0].append(piece)
  print("moving {} from {} to {}".format(piece, loc_temp[1], dest_temp[1]))
  #print(loc, temp, dest)
  
  hanoi(n-1, temp, loc, dest)
  
n = 3
loc = ([3,2,1], "A")
temp = ([], "B")
dest = ([], "C")
hanoi(n, loc, temp, dest)

print(loc, temp, dest)