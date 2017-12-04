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
  curr = arr[0]
  
  while True:

    if arr[curr-1]>0:
        arr[curr-1],curr = -arr[curr-1],abs(arr[curr-1])
    else:
      return abs(arr[curr-1])


print(find_dups_beast_mode([2,4,3,4,2]))
