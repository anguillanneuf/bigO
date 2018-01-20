# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 14:38:00 2018

@author: harrisot
"""

# Recursive solution
def deletion_distance(str1, str2):
  return helper(str1, str2, 0, 0)

def helper(str1, str2, i, j):
  cnt = 0
  
  if i == len(str1): 
    return len(str2[j:])
  if j == len(str2):
    return len(str1[i:])
  
  if str1[i]==str2[j]:
    return helper(str1, str2, i+1, j+1)
  else: 
    cnt += min(helper(str1, str2, i+1, j), 
               helper(str1, str2, i, j+1)) + 1
  return cnt  

str1 = "some"
str2 = "thing"
print(deletion_distance(str1, str2))



# iterative solution 1
def deletion_distance_iterative(s1, s2):
  n1 = len(s1)
  n2 = len(s2)
  mem = [[0 for _ in range(n2+1)] for _ in range(n1+1)]
  
  for i in range(n1+1):
    for j in range(n2+1): 
      if i == 0:
        mem[i][j] = j
      elif j == 0:
        mem[i][j] = i
      elif s1[i-1]==s2[j-1]: 
        mem[i][j] = mem[i-1][j-1]
      else:
        mem[i][j] = 1 + min(mem[i-1][j], mem[i][j-1])
  
  for row in mem: print(row)
  return mem[n1][n2]

print(deletion_distance_iterative("frogog", "dog"))


# iterative solution 2
def deletion_distance_iterative_more_efficient(s1, s2):

  if len(s1) < len(s2): s1,s2 = s2,s1
  
  memo_curr = [None]*(len(s2)+1)
  memo_prev = [None]*(len(s2)+1)
  
  for i in range(len(s1)+1):
    for j in range(len(s2)+1):
      if i == 0: 
        memo_curr[j] = j
      elif j == 0:
        memo_curr[j] = i
      elif s1[i-1]==s2[j-1]:
        memo_curr[j] = memo_prev[j-1]
      else:
        memo_curr[j] = 1+min(memo_prev[j], memo_curr[j-1])

    memo_prev = memo_curr
    memo_curr = [None]*(len(s2)+1)
  return memo_prev[len(s2)]

print(deletion_distance_iterative_more_efficient(str1, str2))