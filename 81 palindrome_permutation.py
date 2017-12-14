#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:26:45 2017

@author: tz
"""

def palindrome_permutation(s):
  mem = dict()
  for ch in s:
    ch = ch.lower()
    if ch==" ": continue # remember the special case of space!
    if ch not in mem.keys():
      mem.update({ch: 1})
    else:
      if mem[ch]==1:
        mem.pop(ch)

  if len(mem)<=1:
    return True
  return False

s = "Tact Coa"
print(palindrome_permutation(s))