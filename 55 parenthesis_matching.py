# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 17:45:18 2017

@author: harrisot
"""

def parenthesis_matching(s, ptr):
  ans = 0
  
  while ptr+1 < len(s):
    ptr += 1
    
    if s[ptr] == ')' and ans == 0:
      return ptr
    
    elif s[ptr] == '(':
      ans += 1
      continue
    
    elif s[ptr] == ')' and ans > 0:
      ans -= 1
      continue
    
  raise Exception("No closing parenthesis")


s = "Sometimes (when I nest them (my parentheticals) too much \
(like this (and this))) they get confusing."

print(parenthesis_matching(s, 10))