#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 22:33:49 2017

@author: tz
"""

def rotate_matrix(mat):
  n = len(mat)
  output = [[0 for _ in range(n)] for _ in range(n)]
  for i in range(n):
    for j in range(n):
      output[j][abs(2-i)]=mat[i][j]  
  return output

mat = [[3,2,1],
       [6,5,4],
       [9,8,7]]

print(rotate_matrix(mat))

"""
[[9,6,3],
 [8,5,2],
 [7,4,1]]
"""