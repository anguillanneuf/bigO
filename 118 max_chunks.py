# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 16:17:32 2018

@author: harrisot


Input: arr = [4,3,2,1,0]
Output: 1
Explanation:
Splitting into two or more chunks will not return the required result.
For example, splitting into [4, 3], [2, 1, 0] will result in [3, 4, 0, 1, 2], 
which isn't sorted.

 0 1 2 3 4
[1,0,2,3,4]
 X X - - - 
 
 0 1 2 3 4 5 6 7 8 9
[1,0,7,2,8,3,5,4,6,9]
 X X|X         X
 
travel to vi=j where the value is vj
if all vals between i and j are <= j, then add |
else: extend j to new j, check condition again
alternatively, find loops!  XXX !WRONG! XXX
do this until j == len(arr)
"""

def max_chunks(arr):
  
  cnt = 0
  i = 0
  j = 0
  t = 0
  _i = -1
  
  for i in range(len(arr)):
    
    if arr[i] > j:
        j = arr[i]
        
    if i == arr[i] and i == j:
        cnt += 1
        t = 0
        _i = i
    else:
        t += 1
        if j-_i == t:
            cnt += 1
        
        
  return cnt

arr1 = [4,3,2,1,0]
arr2 = [1,0,2,3,4]
arr3 = [1,0,7,2,8,3,5,4,6,9]
arr4 = [0,4,5,2,1,3]
arr5 = [1,2,0,3]
arr6 = [1,2,3,4,5,0]
print(arr1, max_chunks(arr1))
print(arr2, max_chunks(arr2))
print(arr3, max_chunks(arr3))
print(arr4, max_chunks(arr4))
print(arr5, max_chunks(arr5))
print(arr6, max_chunks(arr6))
#print([0,1,2], max_chunks([0,1,2]))