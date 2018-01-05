#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 14:34:37 2018

@author: tz
"""

def find_median_in_two_sorted_arr(A,B):
  l = len(A)+len(B)
  if l%2==0:
    return (kth(A,B,l//2-1)+kth(A,B,l//2))/2
  else:
    return kth(A,B,l//2)

def kth(A,B,k):
  print(A,B,k)
  if len(A)>len(B):
    A,B = B,A
    
  if not A:
    return B[k]
  
  if k==len(A)+len(B)-1:
    return max(A[-1],B[-1])
  
  i = len(A)//2       # i+j=k
  j = k-i
  
  if A[i]>B[j]:
    return kth(A[:i],B[j:],i)    # ith because we skip j elements
  else: 
    return kth(A[i:],B[:j],j)    # jth because we skip i elements


A = [1,3,5]
B = [2,4,90]

print(find_median_in_two_sorted_arr(A,B))