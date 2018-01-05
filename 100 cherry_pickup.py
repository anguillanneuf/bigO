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

class Solution:
  def cherryPickup(self, grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    n = len(grid)
    i=j=0
    stack = dict()
    path = [(i,j)]
    stack.update({(i,j): [0 if grid[i][j]==0 else 1, path]})
    
    cherries = 0

    best_path = path
    
    # (0,0) to (n-1,n-1)
    while stack:
      
      (i,j),(c,path) = stack.popitem()
      path_copy = path.copy()
      
      if i==n-1 and j==n-1:
        if c > cherries:
          cherries = c
          best_path = path
      
      if j+1<n and grid[i][j+1]!=-1:
        path.append((i,j+1))
        stack.update({(i,j+1): [max(c+grid[i][j+1], stack[(i,j+1)][0] if (i,j+1) in stack.keys() else 0),
                                path]})
  
      if i+1<n and grid[i+1][j]!=-1:
        path_copy.append((i+1,j))
        stack.update({(i+1,j): [max(c+grid[i+1][j], stack[(i+1,j)][0] if (i+1,j) in stack.keys() else 0),
                                path_copy]})

      
#    print(cherries, best_path)
    
    for (i,j) in best_path:
      grid[i][j]=0
      
#    print(grid)
    i=j=n-1
    stack.update({(i,j):[cherries, best_path]})
    
    while stack:
      (i,j),(c,path) = stack.popitem()
      path_copy = path.copy()
      
      if i==0 and j==0:
        if c > cherries:
          cherries = c
          best_path = path
      
      if j-1>=0 and grid[i][j-1]!=-1:
        path.append((i,j-1))
        stack.update({(i,j-1): [max(c+grid[i][j-1], stack[(i,j-1)][0] if (i,j-1) in stack.keys() else 0),
                                path]})
  
      if i-1>=0 and grid[i-1][j]!=-1:
        path_copy.append((i-1,j))
        stack.update({(i-1,j): [max(c+grid[i-1][j], stack[(i-1,j)][0] if (i-1,j) in stack.keys() else 0),
                                path_copy]})
  
#    print(cherries, best_path)
    return cherries
    
    
grid = [[0, 1, -1],
        [1, 0, -1],
        [1, 1,  1]]  

grid = [[1,1,1,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,1],
        [1,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,0,0,0],
        [0,0,0,1,1,1,1]]
        
mysolution = Solution()
print(mysolution.cherryPickup(grid))