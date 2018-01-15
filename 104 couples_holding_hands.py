#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 14 20:39:55 2018

@author: tz
"""

def check_couple(pair):
    if pair[0]% 2 == 0 and pair[1] - pair[0] == 1:
        return True
    return False

def couples_holding_hands(row):
    swap = 0
    wrong_pairs = []
    
    for i in range(len(row)//2): 
        pair = sorted(row[2*i:2*i+2])
        
        if not check_couple(pair):
            wrong_pairs.append(pair)
        
    wrong_pairs = sorted(wrong_pairs)
    
    while len(wrong_pairs) > 1:
        pair1 = wrong_pairs.pop(0)
        pair2 = wrong_pairs.pop(0)

        if check_couple([pair1[0], pair2[0]]):
            swap += 1
            if not check_couple(sorted([pair1[1], pair2[1]])):
                wrong_pairs.append(sorted([pair1[1], pair2[1]])) 
            
        wrong_pairs = sorted(wrong_pairs)
        
    return swap

print(couples_holding_hands([1,4,0,5,8,7,6,3,2,9]))