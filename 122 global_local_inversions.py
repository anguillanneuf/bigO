# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 10:55:10 2018

@author: harrisot

We have some permutation A of [0, 1, ..., N - 1], 
where N is the length of A.

The number of (global) inversions is the number of i < j 
with 0 <= i < j < N and A[i] > A[j].

The number of local inversions is the number of i 
with 0 <= i < N and A[i] > A[i+1].

# max local inversions = N-1

Return true if and only if the number of global inversions is 
equal to the number of local inversions.

Example 1:
Input: A = [1,0,2]
Output: true
Explanation: There is 1 global inversion, and 1 local inversion.

Example 2:
Input: A = [1,2,0]
Output: false
Explanation: There are 2 global inversions, and 1 local inversion.
Note:

A will be a permutation of [0, 1, ..., A.length - 1].
A will have length in range [1, 5000].
The time limit for this problem has been reduced.
"""

def global_local_inversions(A):
  n_locals = 0
  n_globals = 0
  
  for i in range(len(A)-1):
    if A[i]>A[i+1]:
      n_locals += 1
    for j in range(i+1, len(A)):
      if A[i] > A[j]:
        n_globals += 1
        
  print(n_globals, n_locals)
  return True if n_locals==n_globals else False

A1 = [1,0,2] # g 1, l 1
A2 = [1,2,0] # g 2, l 1
A3 = [2,1,0] # g 3, l 2


for A in [A1, A2, A3]:
  print(global_local_inversions(A))