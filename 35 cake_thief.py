# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 15:56:07 2017

@author: harrisot
"""

def max_duffel_bag_value(cake_tuples, capacity):
    
    
    values = [0] * 600
    
    for weight, value in cake_tuples:
        values[value] += 1
        for i in range(value+1, len(values)):
            
            if weight <= capacity:
                values[i] += values[i-value]
            else:
                exit
            
    print(values)

    for k in range(599, -1, -1):
        if values[k] > 0:
            return k
        
    return -1

cake_tuples = [(7, 160), (3, 90), (2, 15)]
#cake_tuples = [(7,3), (3,1)]
capacity    = 20

print(max_duffel_bag_value(cake_tuples, capacity))