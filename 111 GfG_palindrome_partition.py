# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 11:40:57 2018

@author: harrisot

Given a string, print all possible palindromic partitions

Thinking process for "nitin"

n OK
  i OK
    t OK
    ti X
    tin X
      i OK
      in X
        n OK
  (need to put 'i' back once exits with last n OK)
  it X
  iti OK
    itin X
  itin X
ni X
nit X
niti X
nitin OK
"""

def is_palindrome(s,i,j):
  while i < j:
    if s[i]==s[j]:
      i+=1
      j-=1
    else:
      return False
  return True

def helper(s, prefix, i, n):
  if i==n:
    output = ''
    for p in range(len(prefix)):
      output+=prefix[p][0]+' '
    print(output)
    return
  
  for j in range(i, n):
    if is_palindrome(s, i, j):
      prefix.append([s[i:j+1]])
      helper(s, prefix, j+1, n)
      prefix.pop()

def palindrome_partition(s):
  helper(s, [], 0, len(s))
    

s1 = "nitin"
# n i t i n
# n iti n
# nitin
s2 = "geeks"
# g e e k s
# g ee k s
s3 = "ninin"

for s in [s1,s2,s3]:
  print("Palindrome partitions for {}".format(s))
  palindrome_partition(s)

