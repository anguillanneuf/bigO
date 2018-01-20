# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 14:48:45 2018

@author: harrisot
"""

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
        N = len(grid)
        dp = [[float('-inf')] * N for _ in range(N)]
        dp[0][0] = grid[0][0]
        for t in range(1, 2*N - 1):
            dp2 = [[float('-inf')] * N for _ in range(N)]
            for i in range(max(0, t-(N-1)), min(N-1, t) + 1):
                for p in range(max(0, t-(N-1)), min(N-1, t) + 1):
                    j = t-i
                    q = t-p
                    if grid[i][j] == -1 or grid[p][q] == -1:
                        continue
                    val = grid[i][j]
                    if i != p: val += grid[p][q]
                    dp2[i][p] = max(dp[dp_i][dp_p] + val
                                    for dp_i in (i-1, i) for dp_p in (p-1, p)
                                    if dp_i >= 0 and dp_p >= 0)
                    
                    
            dp = dp2
#            print("when t=", t)
            for row in dp2: print(row)

        return max(0, dp[N-1][N-1])
    
    
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


grid2 = [[1,1,0,-1],
         [0,1,0,1],
         [1,0,0,1],
         [1,1,1,1]]
mysolution = Solution()
print(mysolution.cherryPickup(grid1))
#print(mysolution.cherryPickup(grid2))
#print(mysolution.cherryPickup(grid4)) # 195
