# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 11:29:09 2017

@author: harrisot
"""
import random

def get_random(arr, floor, ceiling):
  i = floor
  j = ceiling + 1
  
  for _ in range(floor, ceiling+1):
    if j - i <= 1:
      exit
    
    random_index = random.randint(i, j)
    arr[i], arr[random_index] = arr[random_index], arr[i]
    i = i + 1
    
  return arr

arr = [1,34,67,32,55,98,72,89]
floor = 3
ceiling = 7
print(get_random(arr, floor, ceiling))