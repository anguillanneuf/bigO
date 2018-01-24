# -*- coding: utf-8 -*-
"""
Created on Wed Jan 24 11:09:00 2018

@author: harrisot

Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, 
because it splits S into less parts.

largest index
0 
a: 0 2 6 8
b:   1 3 5
c:     4 7
9
d: 14
e: 15
f: 11
g: 13
16
h: 19
i: 22
j: 23
k: 20
l: 21

# max index for the lowest char in the remaining arr is 8
# is every other char's max index less than 8
# if yes, partition, update new starting point
# if not, update partition to the max index given by that char

vars to keep track of:
pointer
curr_low
max_idx
remaing

end when pointer reaches the end of the string
"""

def where_to_part(rem, i, j):
  
  left,mid,right = rem[i:].rpartition(rem[j])

  if not set(left) & set(right): 
    return i+len(left)+len(mid)
  else:
    j = i
    for ch in list(set(left)):
      for p, c in enumerate(right):
        if ch == c and j < i+len(left)+p+1:
          j = i+len(left)+p+1
          
    return where_to_part(rem, i, j)
  

def partition_labels(S):
  output = []
  p = 0
  
  while p < len(S):
    q = p
    p = where_to_part(S, q, p)
    output.append(p-q)
    
  return output

#              9      6   0123 
S1 = "ababcbacadefegdehijhklij"
S2 = "caedbdedda"
S3 = "eccbbbbdec"
S4 = "aebbedaddc"
S5 = "qiejxqfnqceocmy"
print(partition_labels(S1))
print(partition_labels(S2))
print(partition_labels(S3))
print(partition_labels(S4))
print(partition_labels(S5))

# 

