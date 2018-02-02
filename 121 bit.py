#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 12:17:51 2018

@author: tz
"""

class Bit(object):
    
    def __init__(self,v):
        self.v = v
        
    def print_binary(self):
        print(format(self.v, '#010b'))
        
    def get_bit(self, k):
        # self.v & (mask) returns true val, not 1 and 0 necessarily
        return 1 if self.v & (1<<k) else 0 
    
    def set_bit(self, k):
        self.v |= (1 << k)
    
    def clear_bit(self, k):
        # Method 1:
#        self.v &= (-1^(1<<k))
        # Method 2:
        self.v &= ~(1 << k)
    
    def clear_bit_above(self, k): 
        # kth to the most significant bit (inclusive)
        self.v &= (1 << k) - 1
    
    def clear_bit_below(self, k):
        # kth to the least significant bit (inclusive)
        self.v &= (-1 << (k + 1))
    
    def update_bit(self, k, bit_value=0):
        self.v |= (bit_value << k)


myBit = Bit(59)
myBit.print_binary()

print(myBit.get_bit(1))

myBit.set_bit(2)
myBit.print_binary()

myBit.clear_bit(2)
myBit.print_binary()

myBit.clear_bit_above(4)
myBit.print_binary()

myBit.clear_bit_below(2)
myBit.print_binary()

myBit.update_bit(7, 1)
myBit.print_binary()


