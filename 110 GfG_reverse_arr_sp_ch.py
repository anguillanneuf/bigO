# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:20:13 2018

@author: harrisot

Reverse an array without affecting special characters

01234
a,b$c
0,2,4
4,2,0
c,b$a

012345678
Ab,c,de!$
0,1,3,5,6
6,5,3,1,0
ed,c,bA!$

"""

def reverse_array_sp_ch(s):
  s = list(s)
  i = 0
  j = len(s)-1
  
  while i<j: 
    if s[i].isalpha():
      if s[j].isalpha():
        s[i], s[j] = s[j], s[i]
        i += 1
        j -= 1
      else:
        j-=1
    else:
      i += 1
      if not s[j].isalpha():
        j-=1

  return ''.join(s)

s1 = "a,b$c"
s2 = "Ab,c,de!$"

print(reverse_array_sp_ch(s1))
print(reverse_array_sp_ch(s2))