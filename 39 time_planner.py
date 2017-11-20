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
  
  if endTime - startTime >= dur:
    return [startTime, startTime + dur]
  else:
    if slotsA[ptrA][1] < slotsB[ptrB][0]:
      return meeting_planner_helper(slotsA, slotsB, dur, ptrA+1, ptrB)
    elif slotsA[ptrA][0] < slotsB[ptrB][1]:
      return meeting_planner_helper(slotsA, slotsB, dur, ptrA, ptrB+1)
    else:
      return meeting_planner_helper(slotsA, slotsB, dur, ptrA+1, ptrB+1)
    
def meeting_planner(slotsA, slotsB, dur):
  return meeting_planner_helper(slotsA, slotsB, dur, 0, 0)  


# iterative
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

slotsA = [[0, 19], [20, 40], [140, 210]]
slotsB = [[1, 13], [35,40]]
dur = 8
#slotsA, slotsB, dur =  [[1,10]], [[2,3],[5,7]], 2

print(meeting_planner(slotsA, slotsB, dur))
print(meetingPlanner(slotsA, slotsB, dur))
  