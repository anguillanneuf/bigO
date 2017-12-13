#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 17:56:24 2017

@author: tz
"""

def contiguous_sequence(arr):
  globalmax = -float('inf')
  localmax = -float('inf')
  for v in arr:
    localmax = max(localmax+v, v)
    if localmax > globalmax:
      globalmax = localmax
  return globalmax

arr = [2,-8,3,-2,4,-10]
print(contiguous_sequence(arr))