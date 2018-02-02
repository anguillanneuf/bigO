#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 10:11:59 2018

@author: tz

Print duplicates in an array of integers going from 0 to 32,000
Memory constraint: 4Kb

4Kbytes = 8 * 4 * 2^10 = 32 * 1024 > 32,000

If we create a bit array of lenght 2^10 of 32-bit integers, we can
effectively monitor which integers have been seen before.
"""

def print_dups_in_arr(arr):
    bitarr = [0]*1024
    for i in arr:
        bucketnum = i >> 5
        assert i//32==i>>5
        
        bitnum = i & 0x1F
        assert i%32==i&0x1F
        
        if bitarr[bucketnum] & (1 << bitnum):
            print(i)
        else:
            bitarr[bucketnum] |= (1 << bitnum)

print_dups_in_arr([3,4,5,6,7,3,6,1,1])

