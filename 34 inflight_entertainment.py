# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 15:29:47 2017

@author: harrisot
"""

def inflight_entertainment(flight, movies):
    movies = set(movies)
    
    for movie in movies:
        if flight - movie in set(movies) and flight != 2*movie:
            return True
    return False

def inflight_entertainment_fast(flight, movies):
    movies_set = set()
    for movie in movies:
        if flight - movie in movies_set:
            return True
        movies_set.add(movie)
    
    return False

print(inflight_entertainment(30, [1,2,3,4]))
print(inflight_entertainment_fast(30, [1,2,3,4]))