# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 13:54:25 2017

@author: harrisot
"""

def helper(s, prefix):
  if len(s) == 0:
    ans.add(prefix)
  for i in range(len(s)):
    helper(s[:i]+s[i+1:], prefix+s[i])

def recursive_string_permuations(s):
  helper(s, '')
  return ans

ans = set()
print(recursive_string_permuations("cat"))
