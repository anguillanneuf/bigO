# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:07:20 2017

@author: harrisot
"""

def permutation_palindrome(s):

  vocab = set()
  
  for i in s:
    if i not in vocab:
      vocab.add(i)
    else:
      vocab.remove(i)
  
  return True if len(vocab) == 1 else False

s1 = "civic"
s2 = "ivicc"
s3 = "civil"
s4 = "livci"

print(permutation_palindrome(s1))
print(permutation_palindrome(s2))
print(permutation_palindrome(s3))
print(permutation_palindrome(s4))