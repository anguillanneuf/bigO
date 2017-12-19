#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:38:05 2017

@author: tz
"""
from functools import reduce
from math import sqrt

def missing_one(arr):
  
  product = reduce(lambda a,b: a+b, arr)
  n = len(arr)
  true_product = reduce(lambda a,b: a+b, range(1,n+2))
  
  return int(true_product-product)

print(missing_one([1,2,4]))

def missing_two(arr):
  n = len(arr)+2
  x_y = n*(n+1)/2-sum(arr)
  xy  = reduce(lambda a,b: a*b, range(1,n+1))/reduce(lambda a,b: a*b, arr)
  print(x_y, xy)
  
  # solve for x,y 
  x = sqrt((x_y)**2/4 -xy)+x_y/2
  y = x_y-x
  return int(x),int(y)

print(missing_two([1,2,3]))
  
  