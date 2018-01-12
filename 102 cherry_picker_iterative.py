# -*- coding: utf-8 -*-
"""
Created on Fri Jan 12 16:14:52 2018

@author: harrisot
"""

class Solution(object):
  def cherry_picker(self, grid):
    n = len(grid)
    memo = [[-float('inf')] * n for _ in range(n)]
    memo[0][0] = grid[0][0]
    
    
    for t in range(1, 2*n-1):
      memo2 = [[-float('inf')] * n for _ in range(n)]
      
      for i in range(max(0,t-n+1), min(n, t+1)):
        
        for p in range(max(0,t-n+1), min(n, t+1)):
          
          j = t-i
          q = t-p
          
          if grid[i][j] < 0 or grid[p][q] < 0: continue

          cherries_present = grid[i][j]
          if i!=p: cherries_present += grid[p][q]

          cherries_past_present_arr = []

          for (dp_i, dp_p) in [(i-1,p-1),(i-1,p),(i,p-1), (i,p)]:
            if dp_i>=0 and dp_p>=0:
              cherries_past_present_arr.append(cherries_present + memo[dp_i][dp_p])
          
          cherries = max(cherries_past_present_arr)
          
          memo2[i][p] = cherries
          
      memo = memo2

    return max(0,memo[n-1][n-1])
  
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
print(mysolution.cherry_picker(grid1))
print(mysolution.cherry_picker(grid2))
print(mysolution.cherry_picker(grid3))