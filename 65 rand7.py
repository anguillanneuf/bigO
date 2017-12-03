#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 12:27:25 2017

@author: tz
"""
import random

def rand5():
  return random.randint(1,5)


def rand7_too_much_space():
  rand = [[1,2,3,4,5],
          [6,7,1,2,3],
          [4,5,6,7,1],
          [2,3,4,5,6],
          [7,1,2,3,4]]
  
  i = rand5() - 1
  j = rand5() - 1
  
  if i == 4 and j > 0:
    return rand7()
  else:
    return rand[i][j]
  
  
def rand7():
  roll1 = rand5()
  roll2 = rand5()
  outcome = (roll1-1)*5+(roll2-1)+1
  if outcome > 21:
    return rand7()
  return outcome%7 + 1
  
print(rand7())
print(rand7())
print(rand7())
print(rand7())
print(rand7())
print(rand7())
print(rand7())