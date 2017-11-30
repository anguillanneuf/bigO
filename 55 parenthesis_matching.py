# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 17:45:18 2017

@author: harrisot
"""

def parenthesis_matching(s, ptr):
  stack = [ptr]
  
  while ptr < len(s):
    ptr += 1
    
    if s[ptr] == '(':
      stack.append(ptr)
    if s[ptr] == ')':
      stack.pop()
    if len(stack)==0:
      break
      
      
  return ptr


s = "Sometimes (when I nest them (my parentheticals) too much \
(like this (and this))) they get confusing."

print(parenthesis_matching(s, 10))