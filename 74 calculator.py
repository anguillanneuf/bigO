#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:03:07 2017

@author: tz
"""

def calculator(equation):
  vals = []
  _vals = []
  ops = []
  _ops = []
  i = 0

  while i < len(equation):
    if not equation[i].isdigit():
      ops.append(equation[i])
      i += 1
    else:
      temp = ''
      while i < len(equation) and equation[i].isdigit(): # important to check int len
        temp += equation[i]
        i += 1
      vals.append(float(temp))
  
  vals = vals[::-1] # important to reverse the array!
  ops = ops[::-1]
  
  while len(ops) > 0:
    op = ops.pop()
    if op == "+" or op == "-":
      _ops.append(op)
      val = vals.pop()
      _vals.append(val)
    else:
      a = vals.pop()
      b = vals.pop()
      if op == "*":
        vals.append(float(a)*float(b))
      else:
        vals.append(float(a)/float(b))
  
  while len(_vals) > 0:
    val = _vals.pop()
    vals.append(val)

  while len(_ops) > 0:
    op = _ops.pop()
    ops.append(op)
    
  while len(ops) > 0:
    op = ops.pop()
    b = vals.pop()
    a = vals.pop()
    if op == "+":
      vals.append(float(a)+float(b))
    else:
      vals.append(float(a)-float(b))
      
  return vals[0]
        
        
print(calculator("2*3+5/6*3+15"))