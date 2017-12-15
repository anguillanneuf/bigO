#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:33:49 2017

@author: tz
"""
def rotate(i,j,mat):
  n = len(mat)
  rollover = mat[i][j]
  
  for k in range(4):
    putaway = mat[j][abs(n-1-i)]
    mat[j][abs(n-1-i)] = rollover
    rollover = putaway
    
    i,j = j,abs(n-i-1)
    
def rotate_matrix(mat):
  n = len(mat)
  
  if n < 2: 
    return mat
  
  for i in range(n-1):
    rotate(0,i,mat)
    if n>=4 and i<n-2:
      rotate(1,n-1-i,mat)
      
  return mat

mat = [[3,2,1],
       [6,5,4],
       [9,8,7]]

print(rotate_matrix(mat))
"""
[[9,6,3],
 [8,5,2],
 [7,4,1]]
"""