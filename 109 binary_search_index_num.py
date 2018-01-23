# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:07:52 2018

@author: harrisot
"""

def index_equals_value_search(arr):
  left = 0
  right = len(arr) - 1
  result = -1
  
  while left < right:

    mid = (right+left)//2
    
    if arr[mid] == mid:
      result = mid
      right = mid-1
    
    if arr[mid] < mid:
      left = mid+1
    
    if arr[mid] >= mid:
      right = mid-1

  return result

arr = [-9,0,2,3,10,29]
print(index_equals_value_search(arr)) # returns 2