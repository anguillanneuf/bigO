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
  