#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:36:37 2017

@author: tz
"""

"""
Merging Ranges

input
---
tuples of integers (start_time, end_time)
[(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]

output
---
[(0, 1), (3, 8), (9, 12)]

"""

def merge_ranges(times):
  times = sorted(times)
  merged = []
  
  for time in times:
    
    if merged == []:
      merged.append(time)
    
    elif merged[-1][0] <= time[0] and time[0] <= merged[-1][1]:
      merged[-1] = (min(merged[-1][0], time[0]), max(merged[-1][1], time[1]))
     
    else:
      merged.append(time)
        
  
  return merged

times = [(0, 1), (3, 5), (4, 8), (10, 12), (9, 10)]
#times = [(1, 2), (2, 3)]
#times = [(1, 5), (2, 3)]
#times = [(1, 10), (2, 6), (3, 5), (7, 9)]
print(merge_ranges(times))