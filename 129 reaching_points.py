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
        if sx > sy: 
            sx, sy = sy, sx
        if tx > ty:
            tx, ty = ty, tx
            
        mem = set()
        mem.add((sx, sy))
        
        while mem:
            if (tx, ty) in mem:
                return True
            
            new_mem = set()
            while mem:
                a,b = mem.pop()
                self.expand(a, b, new_mem)
                
            good_mem = set()
            for a, b in sorted(new_mem):
                if self.check_cond(a, b, tx, ty):
                    good_mem.add((a, b))
            
            mem = good_mem
            
        return False


    def expand(self, x, y, mem):
        	mem.add(tuple(sorted([x+y, y])))
        	mem.add(tuple(sorted([x, y+x])))
          
    def check_cond(self,sx, sy, tx, ty):
        cond = False
        if sx < tx and sy < ty:
            cond = True
        elif sx==tx:
            if sy < ty:
                cond = True
            elif sy==ty:
                cond = True
            else:
                cond = False
        else:
            cond = False
        return cond
    

sx = 1; sy = 1; tx = 2; ty = 1
sx = 1; sy = 1; tx = 3; ty = 5
sx = 9; sy = 5; tx = 12; ty = 9
#sx=35
#sy=13
#tx=455955547
#ty=420098884
s = Solution()
print(s.reachingPoints(sx, sy, tx, ty))
