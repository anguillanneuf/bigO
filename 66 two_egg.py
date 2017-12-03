#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:52:24 2017

@author: tz
"""

def two_egg_problem():
  """100 floors, find the highest floor an egg can be dropped without breaking"""
  x = 0
  while (1+x)*x//2 < 100:
    x+=1
  return x

print(two_egg_problem())