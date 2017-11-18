#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 22:52:35 2017

@author: tz
"""

def is_match(text, pattern):
    return is_match_helper(text, pattern, 0, 0)

def is_match_helper(text, pattern, i, j):
  
  if i >= len(text):
      if j >= len(pattern): 
          return True
      elif j+1<len(pattern) and pattern[j+1]=='*':
          return is_match_helper(text, pattern, i, j+2)
      else:
          return False
      
  elif j>=len(pattern) and i<len(text):
      return False
  
  elif j+1<len(pattern) and pattern[j+1]=='*':
      if pattern[j]=='.' or text[i]==pattern[j]:
          return is_match_helper(text, pattern, i, j+2) or \
                  is_match_helper(text, pattern, i+1, j)
      else:
          return is_match_helper(text, pattern, i, j+2)
      
  elif pattern[j]=='.' or text[i]==pattern[j]:
      return is_match_helper(text, pattern, i+1, j+1)
  
  else:
      return False

print(is_match("aa", "a"))
print(is_match("aa", "aa"))
print(is_match("abc", "a.c"))
print(is_match("abbb", "ab*"))
print(is_match("abbbbbf", "ab.*f"))
print(is_match("abaa", "a.*a*"))
print(is_match("abbdbb", "ab*d"))
print(is_match("abcbc", ".*bc"))
print(is_match("abc", "abcd*"))