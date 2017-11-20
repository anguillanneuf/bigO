# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:19:23 2017

@author: harrisot
"""

def meeting_planner_helper(slotsA, slotsB, dur, ptrA, ptrB):
  if ptrA >= len(slotsA) or ptrB >= len(slotsB): 
    return []
  
  startTime = max(slotsA[ptrA][0], slotsB[ptrB][0])
  endTime = min(slotsA[ptrA][1], slotsB[ptrB][1])
  if endTime - startTime < dur:
    if slotsA[ptrA][1] < slotsB[ptrB][0]:
      return meeting_planner_helper(slotsA, slotsB, dur, ptrA+1, ptrB)
    else: 
      return meeting_planner_helper(slotsA, slotsB, dur, ptrA, ptrB+1)
  else:
    return [startTime, startTime+dur]
def meeting_planner(slotsA, slotsB, dur):
	return meeting_planner_helper(slotsA, slotsB, dur, 0, 0)  


slotsA = [[0, 10], [20, 40], [140, 210]]
slotsB = [[12, 18], [30,40]]
dur = 8

print(meeting_planner(slotsA, slotsB, dur))
  