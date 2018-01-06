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
4 cherries were picked up during this single trip, and the matrix becomes [[0,1,-1],[0,0,-1],[0,0,0]].
Then, the player went left, up, up, left to return home, picking up one more cherry.
The total number of cherries picked up is 5, and this is the maximum possible.

"""

class Solution(object):
    def cherryPickup(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        if grid[0][0]==-1: return 0
        
        self.grid = grid
        self.memo = {}
        self.N = len(grid)
        ans = max(self.helper(0,0,0,0), 0)
#        print(self.memo)
        return ans


    def helper(self,i1,j1,i2,j2):
        
        if (i1,j1,i2,j2) in self.memo: return self.memo[(i1,j1,i2,j2)]
        
        N = self.N
        if i1 == N or j1 == N or i2 == N or j2 == N: return -1
        if i1 == N-1 and j1 == N-1 and i2 == N-1 and j2 == N-1: return self.grid[-1][-1]
        if self.grid[i1][j1] == -1 or self.grid[i2][j2] == -1: return -1
        
        # now can take a step in two directions at each end, which amounts to 4 combinations in total
        dd = self.helper(i1+1, j1, i2+1, j2)
        dr = self.helper(i1+1, j1, i2, j2+1)
        rd = self.helper(i1, j1+1, i2+1, j2)
        rr = self.helper(i1, j1+1, i2, j2+1)
        maxComb = max([dd, dr, rd, rr])
        
        # find if there is a way to reach the end
        if maxComb == -1:
            out = -1
        else:
            # same cell, can only count this cell once
            if i1 == i2 and j1 == j2:
                out = maxComb + self.grid[i1][j1]
            # different cell, can collect both
            else:
                out = maxComb + self.grid[i1][j1] + self.grid[i2][j2]
                
        # cache result
        self.memo[(i1, j1, i2, j2)] = out
        return out
    
    
grid = [[0, 1, -1],
        [1, 0, -1],
        [1, 1,  1]]  

#grid = [[1,1,1,1,0,0,0],
#        [0,0,0,1,0,0,0],
#        [0,0,0,1,0,0,1],
#        [1,0,0,1,0,0,0],
#        [0,0,0,1,0,0,0],
#        [0,0,0,1,0,0,0],
#        [0,0,0,1,1,1,1]]
        
mysolution = Solution()
print(mysolution.cherryPickup(grid))