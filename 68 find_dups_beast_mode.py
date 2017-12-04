#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 21:57:08 2017

@author: tz
"""
class LinkedList:
  def __init__(self, value):
    self.value = value
    self.next = None

def find_dups_beast_mode(arr):

  for curr in arr:

    if arr[abs(curr)-1]>0:
        arr[abs(curr)-1] = -arr[abs(curr)-1]
    else:
      return abs(curr)

print(find_dups_beast_mode([1,2,3,4,2]))
print(find_dups_beast_mode([2,2,1,3]))