# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 11:34:52 2017

@author: harrisot
"""
def bracket_validator(s):
  openers = {'(':0, '{':0, '[':0}
  closers = {')':'(', '}':'{', ']':'['}
  stack = []
  
  i = 0
  
  while i < len(s):
    
    if s[i] in openers.keys():
      stack.append(s[i])
    elif s[i] in closers.keys():
      if closers[s[i]] == stack[-1]: 
        stack.pop()
    if i == len(s)-1 and len(stack)==0:
      return True
    
    i += 1
  
  return False

s1 = "{ [ ] ( ) }"
s2 = "{ [ ( ] ) }"
s3 = "{ [ }"
s4 = "{ [ ( ] ) }"

print(bracket_validator(s1))
print(bracket_validator(s2))
print(bracket_validator(s3))
print(bracket_validator(s4))