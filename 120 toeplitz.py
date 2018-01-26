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
    m = len(M)
    n = len(M[0])
    
    if n >=m: 
            
        for k in range(n-1):
            i = 0
            j = k
            v = M[i][j]
            
            while i <= m-1 and j <= n-1:
                if M[i][j]==v:
                    i+=1
                    j+=1
                else:
                    return False
                
        for k in range(n-1,0,-1):
            i = m-1
            j = k
            v = M[i][j]
            
            while i>=0 and j>=0:
                if M[i][j]==v:
                    i-=1
                    j-=1
                else:
                    return False
    else:
        
        for k in range(m-1):
            i = k
            j = 0
            v = M[i][j]
            
            while i <= m-1 and j <= n-1:
                if M[i][j]==v:
                    i+=1
                    j+=1
                else:
                    return False
                
        for k in range(m-1,0,-1):
            i = k
            j = n-1
            v = M[i][j]
            
            while i>=0 and j>=0:
                if M[i][j]==v:
                    i-=1
                    j-=1
                else:
                    return False
        
    return True


M1 = [[1,2,3,4],[5,1,2,3],[9,5,1,2]]
M2 = [[1,2],[2,2]]
M3 = [[97,97],[80,97],[10,80]]
M4 = [[36,59,71,15,26,82,87],[56,36,59,71,15,26,82],[15,0,36,59,71,15,26]]
M5 = [[44,35,39],[15,44,35],[17,15,44],[80,17,15],[43,80,0],[77,43,80]]
M6 = [[20,45,14,13,6,4],[48,20,45,14,13,6],[22,48,20,45,14,13],[46,22,48,20,45,14],[82,46,22,48,20,45],[39,0,46,22,48,20]]
for row in M6: print(row)
for M in [M1, M2, M3, M4, M5, M6]:
    print(toeplitz(M))