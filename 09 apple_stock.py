#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 21:59:21 2017

@author: tz
"""


def get_max_profit(prices):
    
    if len(prices) < 2:
        return("Not enough data points!")
    
    i = 0
    min_price = prices[i]
    max_profit = prices[i+1]-prices[i]
    
    while i < len(prices):
        profit = prices[i]-min_price
        
        if profit > max_profit:
            max_profit = profit

        if prices[i] < min_price:
            min_price = prices[i]
            
        i += 1
        
    return max_profit


prices = [12,3,6,14,1,11,10]
print(get_max_profit(prices))