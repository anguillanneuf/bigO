# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 15:56:07 2017

@author: harrisot
"""

def max_duffel_bag_value(cake_tuples, capacity):
  if capacity == 0: return 0
  
  cake_dict = {weight: value for (weight, value) in cake_tuples}
  weights = [0] * capacity

  for weight, value in sorted(cake_tuples):
    weights[weight-1] += cake_dict.get(weight)
    
    for i in range(weight, len(weights)):
      temp = weights[i-weight] + cake_dict.get(weight)
      if temp > weights[i]:
        weights[i] = temp
#  print(weights)
  return max(weights)

cake_tuples = [(7, 160), (3, 90), (2, 15)]
capacity    = 20

print(max_duffel_bag_value(cake_tuples, capacity))