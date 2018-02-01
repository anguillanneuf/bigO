# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:13:52 2018

@author: harrisot

Given an array arr of integers (not necessarily distinct), 
we split the array into some number of "chunks" (partitions), 
and individually sort each chunk.  
After concatenating them, the result equals the sorted array.

What is the most number of chunks we could have made?

Example 1:

Input: arr = [5,4,3,2,1]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [5, 4], [3, 2, 1] will result in 
[4, 5, 1, 2, 3], which isn't sorted.
Example 2:

Input: arr = [2,1,3,4,4]
Output: 4
Explanation:
We can split into two chunks, such as [2, 1], [3, 4, 4].
However, splitting into [2, 1], [3], [4], [4] is the highest number 
of chunks possible.
Note:

arr will have length in range [1, 2000].
arr[i] will be an integer in range [0, 10**8].
"""
from collections import Counter

def max_chunks_with_dups(arr):
  ans, c1, c2 = 0, Counter(), Counter()
  for i,j in zip(arr, sorted(arr)):
    c1[i] +=1
    c2[j] +=1
    ans += c1==c2
  return ans

arr1 = [5,4,3,2,1]
arr2 = [2,1,3,4,4]
arr3 = [4,2,2,1,1]
arr4 = [1,1,0,0,1]
arr5 = [0,0,1,1,0,1,1,1,1,0]
for arr in [arr1, arr2, arr3, arr4, arr5]:
  print(arr, max_chunks_with_dups(arr))


