#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 11 11:10:55 2018

@author: tz

A move consists of taking a point (x, y) and transforming it to either (x, x+y) or (x+y, y).

Given a starting point (sx, sy) and a target point (tx, ty), 
return True if and only if a sequence of moves exists to transform the point (sx, sy) to (tx, ty). 
Otherwise, return False.

Examples:
Input: sx = 1, sy = 1, tx = 3, ty = 5
Output: True
Explanation:
One series of moves that transforms the starting point to the target is:
(1, 1) -> (1, 2)
(1, 2) -> (3, 2)
(3, 2) -> (3, 5)

Input: sx = 1, sy = 1, tx = 2, ty = 2
Output: False

Input: sx = 1, sy = 1, tx = 1, ty = 1
Output: True

Note:

sx, sy, tx, ty will all be integers in the range [1, 10^9].

"""



class Solution:
    def reachingPoints(self, sx, sy, tx, ty):
        """
        :type sx: int
        :type sy: int
        :type tx: int
        :type ty: int
        :rtype: bool
        """
     
        while sx < tx and sy < ty:
            tx, ty = tx%ty, ty%tx
            print(tx, ty)
            
        if (ty-sy)%sx==0 and tx==sx or \
            (tx-sx)%sy==0 and ty==sy:
            return True
        else:  
            return False



    

sx = 1; sy = 1; tx = 1000000000; ty = 1
#sx = 1; sy = 1; tx = 3; ty = 5
#sx = 9; sy = 5; tx = 12; ty = 9
#sx=35;sy=13;tx=455955547;ty=420098884
#sx = 3; sy = 7; tx = 10; ty = 27
#sx = 2; sy = 4; tx = 15; ty = 9
s = Solution()
print(s.reachingPoints(sx, sy, tx, ty))
