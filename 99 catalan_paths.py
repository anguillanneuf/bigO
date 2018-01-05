#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:12:00 2018

@author: tz
"""

def paths(n):
  mat = [[0 for i in range(n)] for i in range(n)]
  
  for i in range(n-1,-1,-1):
    for j in range(n-i-1,n):
      if i==n-1:
        mat[i][j]=1
      else:
        mat[i][j]=mat[i][j-1]+mat[i+1][j]     
  
  return mat[0][n-1]

print(paths(5))