# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 12:07:20 2017

@author: harrisot
"""

def permutation_palindrome(s):
  vocab = {}
  
  
  for i in s:
    
    if i not in vocab.keys():
      vocab.update({i: 1})
    else:
      vocab[i] = (vocab[i] + 1) % 2
  
  return True if sum([v for v in vocab.values()]) == 1 else False

s1 = "civic"
s2 = "ivicc"
s3 = "civil"
s4 = "livci"

print(permutation_palindrome(s1))
print(permutation_palindrome(s2))
print(permutation_palindrome(s3))
print(permutation_palindrome(s4))