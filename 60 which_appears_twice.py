# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:42:19 2017

@author: harrisot
"""

def which_appears_once(arr):
  temp = 0
  for k in arr:
    temp ^= k
  return temp
  
def which_appears_twice(arr,n):
  return int(sum(arr)-n*(n+1)/2)
  

print(which_appears_once([23,45,65,2,45,2,23]))
print(which_appears_twice([1,2,3,4,5,4],5))