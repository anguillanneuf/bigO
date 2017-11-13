#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 12 22:20:52 2017

@author: tz
"""

my_rectangle = {

    # coordinates of bottom-left corner
    'left_x': 1,
    'bottom_y': 1,

    # width and height
    'width': 10,
    'height': 10,

}

my_rectangle2 = {

    # coordinates of bottom-left corner
    'left_x': 4,
    'bottom_y': 4,

    # width and height
    'width': 3,
    'height': 15,

}
  
def rectangle_love(rec1, rec2):
    
    left_x = (max(rec1.get('left_x'), rec2.get('left_x')))
    bottom_y = (max(rec1.get('bottom_y'), rec2.get('bottom_y')))
    right_x = (min(rec1.get('left_x')+rec1.get('width'), rec2.get('left_x')+rec2.get('width')))
    top_y = (min(rec1.get('bottom_y')+rec1.get('height'), rec2.get('bottom_y')+rec2.get('height')))
    
    rec = {
            'left_x':  left_x,
            'bottom_y': bottom_y,
            
            'width': right_x - left_x,
            'height': top_y - bottom_y
            }
    
    if rec.get('width') <= 0 or rec.get('height') <= 0:
        return "No overlap!"
        
    
    return rec

print(rectangle_love(my_rectangle, my_rectangle2))

