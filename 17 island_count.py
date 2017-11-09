#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  8 22:25:16 2017

@author: tz
"""

def search(mat, i, j, m, n):
  
  if i > -1 and i < m and j > -1 and j < n:
    if mat[i][j] == 1:
      mat[i][j] = 0
      search(mat, i+1, j, m, n)
      search(mat, i, j+1, m, n)
      search(mat, i-1, j, m, n)
      search(mat, i, j-1, m, n)

def get_number_of_islands(binaryMatrix):
  m,n = len(binaryMatrix), len(binaryMatrix[0])
  count = 0
  
  for i in range(m):
    for j in range(n):
      if binaryMatrix[i][j]==1:
        search(binaryMatrix, i, j, m, n)
        count += 1
  return count
    
binaryMatrix = [ [0,    1,    0,    1,    0],
                         [0,    0,    1,    1,    1],
                         [1,    0,    0,    1,    0],
                         [0,    1,    1,    0,    0],
                         [1,    0,    1,    0,    1] ]

print(get_number_of_islands(binaryMatrix))