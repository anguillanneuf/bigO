#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec  9 17:14:04 2017

@author: tz
"""

def permutations(s, prefix):
  if s == "":
    print(prefix)
  else:
    for i in range(len(s)):
      permutations(s[:i]+s[i+1:], prefix+s[i])

print("Permutaitons without dups: ")
permutations('caa', '')



def permutations_with_duplicates(n, prefix, mem):
  if n == 0:
    print(prefix)
    
  else:
    for char in mem.keys():
      if mem[char]>0:
#        print(mem)
        mem[char] -= 1
        permutations_with_duplicates(n-1, prefix+char, mem)
#        print(mem)
        mem[char] += 1

mem = dict()    
for i in 'caa':
  if i not in mem.keys():
    mem.update({i: 1})
  else:
    mem[i] += 1

print("Permutations with dups:")
permutations_with_duplicates(3, '', mem)