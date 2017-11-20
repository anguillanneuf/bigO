# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 16:19:23 2017

@author: harrisot
"""
def meetingPlanner(slotsA, slotsB, dur):
  ia = 0
  ib = 0
  while (ia < len(slotsA) and ib < len(slotsB)):
    start = max(slotsA[ia][0], slotsB[ib][0])
    end = min(slotsA[ia][1], slotsB[ib][1])

    if (start + dur <= end):
      return [start, start + dur]

    if (slotsA[ia][1] < slotsB[ib][1]):
      ia+=1
    else:
      ib+=1

  return []

slotsA = [[0, 1], [2, 40], [140, 210]]
slotsB = [[1, 13], [35,40]]
dur = 8
print(meetingPlanner(slotsA, slotsB, dur))

# recursive approach
def meeting_planner_helper(slotsA, slotsB, dur, ptrA, ptrB):  
  if ptrA >= len(slotsA) or ptrB >= len(slotsB): 
    return []
  
  startTime = max(slotsA[ptrA][0], slotsB[ptrB][0])
  endTime = min(slotsA[ptrA][1], slotsB[ptrB][1])

  if endTime - startTime < dur:
    if slotsA[ptrA][1] < slotsB[ptrB][1]:
      return meeting_planner_helper(slotsA, slotsB, dur, ptrA+1, ptrB)
    else:
      return meeting_planner_helper(slotsA, slotsB, dur, ptrA, ptrB+1)
  else: 
    return [startTime, startTime+dur]
    
def meeting_planner(slotsA, slotsB, dur):
  return meeting_planner_helper(slotsA, slotsB, dur, 0, 0) 

print(meeting_planner(slotsA, slotsB, dur))
  