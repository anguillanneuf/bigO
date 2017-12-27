# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 15:54:06 2017

@author: harrisot

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
  
  
  # 1. converts arr into binary arr
  n = len(arr)
  nb = int(log(n,2))
  fmt = '#0'+str(int(nb+1+2))+'b'
  arr_b = [format(v, fmt) for v in arr]
  result = [0]*int(nb+1)
  
  # 2. deduces the rightmost binary digit of the missing value
  i = -1
  c0 = c1 = 0
  for v in arr_b:
    if v[i]=="0": 
      c0+=1
    else: c1+=1

  if c0<=c1:
    d = 0
  else: d = 1
    
  # 3. determines the earlsier binary digits (HARD)
  result[-1] = d
  for i in range(-2, int(-nb-2), -1):    
    arr_b = [v for v in arr_b if v[i+1]==str(d)]
    c0=c1=0
    for v in arr_b:
      if v[i]=="0":
        c0+=1
      else: c1+=1
    if c0<=c1:
      d = 0
    else:
      d = 1
    result[i] = d
    print(arr_b, result)
  
  # 4. convert result to base 10

  power = nb
  output = 0
  for v in result:
    output += v*2**power
    power-=1
  
  return int(output)

arr = [0,1,2,3,4,5,6,7,8,9,10,11,12,14,15]
print(missing_number(arr))