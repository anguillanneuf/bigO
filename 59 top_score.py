# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:01:42 2017

@author: harrisot
"""

def helper_ascending(arr, exponent):
  """Radix sort: O(n+k) """
  temp = [0] * len(arr)
  count = [0] * 10
  
  for z in arr:
    y = z // exponent
    count[y%10] += 1
    
  print("Step 1: ",  count)
  
  for i in range(1,10):
    count[i] += count[i-1]
    
  print("Step 2: ", count)
  
  #for i in range(len(arr)):
  for i in range(len(arr)-1, -1, -1):
    print("intermediate temp: ", temp)
    print("intermediate count: ", count)
    j = arr[i]//exponent
    print("j: ", j)
    temp[count[j%10]-1] = arr[i]
    print("count[j%10]-1: ", count[j%10]-1)
    count[j%10] -= 1
    
  print("Step 3:", count)
  print("Sorted: ", temp)
  
  for i in range(len(temp)):
    arr[i] = temp[i]

def helper_descending(arr, exponent):
  """Radix sort; O(n)"""
  temp = [0] * len(arr)
  count = [0] * 10
  
  for z in arr:
    y = z//exponent
    count[y%10] += 1
  #print("Step 1: ",  count)
  
  for i in range(8,-1,-1):
    count[i] += count[i+1]
  #print("Step 2: ",  count)
  
  for i in range(len(temp)-1,-1,-1):
    y = arr[i]//exponent
    temp[count[y%10]-1] = arr[i]
    count[y%10] -= 1
  #print("Step 3: ",  count)
  #print("temp: ", temp)
  
  for i in range(len(temp)):
    arr[i] = temp[i]

def sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
  for i in range(3):
    helper_descending(unsorted_scores, 10**i)
  return unsorted_scores


def counting_sort(unsorted_scores, HIGHEST_POSSIBLE_SCORE):
  temp = [0]*(HIGHEST_POSSIBLE_SCORE+1)
  sorted_scores = []
  
  for score in unsorted_scores:
    temp[score] += 1
    
  for i in range(HIGHEST_POSSIBLE_SCORE, -1, -1):
    if temp[i] > 0:
      for j in range(temp[i]):
        sorted_scores.append(i)
        
  return sorted_scores
  

unsorted_scores = [37, 89, 41, 65, 91, 53]
HIGHEST_POSSIBLE_SCORE = 100

print(sort_scores(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
print(counting_sort(unsorted_scores, HIGHEST_POSSIBLE_SCORE))
# returns [91, 89, 65, 53, 41, 37]