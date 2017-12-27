# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:54:06 2017

@author: harrisot

Question 17.4 in Cracking the Coding Interview

00000
00001
00010
00011
00100
00101
00110
00111
01000
01001
01010
01011
01100
01101
01110
01111
10000

Notice how:
- 0s and 1s oscillate 2^0 number in position 2^0: 0,1,0,1...
- 0s and 1s oscillate 2^1 number in position 2^1: 0,0,1,1,0,0...
- 0s and 1s oscillate 2^2 number in position 2^2: 0,0,0,0,1,1,1,1...
- 0s and 1s oscillate 2^3 number in position 2^3: 0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1...
"""
from math import log

def missing_number(arr):
  
  n = len(arr) 
  nbits = int(log(n,2)+1)            # no. of bits needed to store max v in array 
  fmt = '#0'+str(int(nbits+2))+'b'   # format to represent values in binary, e.g. '#05b'
  result = 0
  d = None
  
  # determines the binary digits from right to left
  for i in range(-1, int(-nbits-1), -1):
    c0 = c1 = 0               # set the count for zeros and ones to be 0
    
    if i == -1:               # preprocesses arr to binary format
      arr = [format(v, fmt) for v in arr]
    elif d is not None:       # eliminates values whose i-th bit is d
      arr = [v for v in arr if v[i+1]==str(d)]
    
    for v in arr:             # update the counts for zeros and ones for i-th bit
      if v[i]=="0":
        c0+=1
      else: c1+=1
    if c0<=c1:
      d = 0
    else: d = 1
    
    result += d*2**abs(i+1)  # converts the correctly determined value at the i-th bit to decimal 
  
  return result

arr1 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
print(missing_number(arr1)) # should print 16
arr2 = [0,1,2,3,4,5,6,7,9,10,11,12,13,14,15]
print(missing_number(arr2)) # should print 8