#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 14:55:41 2017

@author: tz
"""
def optimize(i, boxes, mem):
 
  if i == 0:
    mem[i] =boxes[i][2]
    return mem[i]
  
  tallest = boxes[i][2]
  
  for j in range(i-1,-1,-1):  
    if boxes[j][1] <= boxes[i][1]:
      tallest = max(tallest, mem[j]+boxes[i][2])
      break
    
  mem[i]= tallest

  return tallest

def optimize_height(boxes):
  boxes = sorted(boxes)
  print(boxes)
  tallest = 0
  mem = [0 for i in range(len(boxes))]
  
  for i in range(len(boxes)):
    temp = optimize(i, boxes, mem)
    if temp > tallest:
      tallest = temp

  return tallest

boxes = [(30,20,5),(10,20,3),(10,40,1),(50,20,4),(20,60,7)]

print(optimize_height(boxes))