#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 11:49:00 2018

@author: tz
"""

def selfDividingNumbers(left, right):
    """
    :type left: int
    :type right: int
    :rtype: List[int]
    """
    ans = []
    
    for num in range(left, right+1):

        good = True
        num_copy = num
        
        while num > 0:
            if num % 10 == 0:
                good = False
                break
            
            if num_copy % (num % 10) == 0:
                num //= 10
            else:
                good = False
                break
                
        if good:
            ans.append(num_copy)
            
    return ans

print(selfDividingNumbers(1,22))