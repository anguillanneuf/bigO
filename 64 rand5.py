# -*- coding: utf-8 -*-
"""
Created on Fri Dec  1 16:49:02 2017

@author: harrisot
"""

import random

def rand7():
  return random.randint(1,7)

def rand5():
  temp = 7
  while temp > 5:
    temp = rand7()
  return temp

print(rand5())
