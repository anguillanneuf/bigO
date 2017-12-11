#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 10 20:03:07 2017

@author: tz
"""
import operator

def operate(op):
  return {'+': operator.add, 
          '-': operator.sub,
          '*': operator.mul,
          '/': operator.truediv}[op]

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
      vals.append(operate(op)(a,b))
  
  while len(_vals) > 0:
    val = _vals.pop()
    vals.append(val)

  while len(_ops) > 0:
    op = _ops.pop()
    ops.append(op)
    
  while len(ops) > 0:
    op = ops.pop()
    a = vals.pop()
    b = vals.pop()
    vals.append(operate(op)(a,b))

  return vals[0]
        
print(calculator("2*3+5/6*3+15"))

def calculator_super(equation):
  i = 0
  vals = []
  ops = []
  
  while i < len(equation):
    
    symbol = ''
    while i < len(equation) and equation[i].isdigit():
      symbol += equation[i]
      i += 1
    if symbol != '':
      vals.append(float(symbol))
    
    if i < len(equation) and not equation[i].isdigit():
      ops.append(equation[i])
      i += 1
    
    if ops[-1]=='*' or ops[-1]=='/':
      symbol = ''
      while i < len(equation) and equation[i].isdigit():
        symbol += equation[i]
        i += 1
      vals.append(float(symbol))
      
      op = ops.pop()
      b = vals.pop()
      a = vals.pop()
      
      vals.append(operate(op)(a,b))
  
  for _ in range(len(ops)):
    b = vals.pop()
    a = vals.pop()
    op = ops.pop()
    vals.append(operate(op)(a,b))
    
  return vals[0]


print(calculator_super("2*3+5/6*3+15"))
#print(calculator_super("1985/5-1983/8+9/4"))