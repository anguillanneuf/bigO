#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  5 10:29:42 2018

@author: tz

Input: grid =
[[0, 1, -1],
 [1, 0, -1],
 [1, 1,  1]]
Output: 5
Explanation: 
The player started at (0, 0) and went down, down, right right to reach (2, 2).
4 cherries were picked up during this single trip, and the matrix becomes 
[[0,1,-1],
 [0,0,-1],
 [0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.
"""

class Solution(object):
    def cherryPickup(self, grid):
        self.memo = {}
        self.grid = grid
        return max(self.dp(0,0,0,0),0)
    
    def dp(self,i,j,p,q):
        """Given two starting cells (i,j) and (p,q), return the max # 
        of cherries from them to (n-1,n-1)
        """
        
        if (i,j,p,q) in self.memo: return self.memo[(i,j,p,q)]
        
        N = len(self.grid)
        if any(o==N for o in [i,j,p,q]): return -1                     # out of bound
        
        if all(o==N-1 for o in [i,j,p,q]): return self.grid[N-1][N-1]  # reach destination
        # Note: in order for this to condition to ever be true
        # (i,j) and (p,q) must be equally distant from (n-1,n-1)
        # Feel free to change line 27 to max(self.dp(0,1,1,0),0) and it will work
        # However, if i+j!=p+q, the result will not be satisfactory
        
        if self.grid[i][j]==-1 or self.grid[p][q]==-1: return -1       # hit a thorn
        
        dd = self.dp(i+1,j,p+1,q)
        dr = self.dp(i+1,j,p,q+1)
        rd = self.dp(i,j+1,p+1,q)
        rr = self.dp(i,j+1,p,q+1)
        
        maxCherries = max(dd, dr, rd, rr)
        
        if maxCherries == -1:
            out = -1
        else:
            if i==p and j==q: # same cell
                out = maxCherries + self.grid[i][j]
            else:
                out = maxCherries + self.grid[i][j] + self.grid[p][q]
        
        """memo stores starting positions and the max # of cherries given such 
        starting positions
        """
        self.memo.update({(i,j,p,q):out})
        return out
    
    
grid1 = [[0, 1, -1],
         [1, 0, -1],
         [1, 1,  1]]  

grid2 = [[1,1,0],
         [0,1,0],
         [1,0,0]]

grid3 = [[1,1,1,1,0,0,0],
         [0,0,0,1,0,0,0],
         [0,0,0,1,0,0,1],
         [1,0,0,1,0,0,0],
         [0,0,0,1,0,0,0],
         [0,0,0,1,0,0,0],
         [0,0,0,1,1,1,1]]
        
mysolution = Solution()
print(mysolution.cherryPickup(grid1))
print(mysolution.cherryPickup(grid3))
print(mysolution.cherryPickup(grid2))
print(mysolution.memo)