#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 26 16:52:20 2018

@author: tz

Input: matrix = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
Output: True
Explanation:
1234
5123
9512

In the above grid, the diagonals are "[9]", "[5, 5]", "[1, 1, 1]", "[2, 2, 2]", 
"[3, 3]", "[4]", and in each diagonal all elements are the same, so the answer is True.

"""
def toeplitz(M):
    n = len(M)
    m = len(M[0])
    
    if n==1 or m==1:
        return True
    
    for i in range(1, n):
        prev = M[i-1][:m-1]
        curr = M[i][1:m]
        if prev!=curr:
            return False
        
    return True


M1 = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
M2 = [[1,2],[2,2]]
M3 = [[97,97],[80,97],[10,80]]
M4 = [[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]]
M5 = [[44,35,39],[15,44,35],[17,15,44],[80,17,15],[43,80,0],[77,43,80]]
M6 = [[20,45,14,13,6,4],[48,20,45,14,13,6],[22,48,20,45,14,13],[46,22,48,20,45,14],[82,46,22,48,20,45],[39,0,46,22,48,20]]
for M in [M1, M2, M3, M4, M5, M6]:
    for row in M: print(row)
    print(toeplitz(M))