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
  """Because locals are always globals, if there are
	only locals, return True. 
	Only locals mean we only allow the greater-than (>) 
	relationship to exist between numbers that are next to 
	each other, never number that are farther apart than that.
   This is a *greedy* solution. """
    
  cmax = 0
  for i in range(len(A)-2):
    cmax = max(cmax, A[i])
    if cmax > A[i+2]:
      return False
  return True

A1 = [1,0,2]
A2 = [1,2,0] 
A3 = [2,1,3,0,4] 
A4 = [5,0,1,2,3,4]
A5 = [4,5,0,1,2,3] 
A6 = [1,0,3,2,5,4]

for A in [A1, A2, A3, A4, A5, A6]:
  print(global_local_inversions(A))