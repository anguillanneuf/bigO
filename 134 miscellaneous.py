#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 19 13:04:43 2018

@author: tianzi
"""
# =============================================================================
# Find rank order of items in an array
# =============================================================================

x = [2,1,3,1,4]

# return indices of the sorted x by the sorted x's positions
y = sorted(range(len(x)), key=x.__getitem__)
print(y) # [1, 3, 0, 2, 4]

# return indices of the sorted x by the unsorted x's positions
z = [0] * len(x)
for i,v in enumerate(y):
    z[v] = i
print(z) # [2, 0, 3, 1, 4], for examples, x[1] ranks 0th, x[3] ranks 1st, so on

# =============================================================================
# Python dictionary has `get` and `__getitem__`
# =============================================================================

x = {'nyc': 1, 'sf': 2, 'boston': 3, 'sgp': 4}

print(sorted(x, key=x.__getitem__)) # ['nyc', 'sf', 'boston', 'sgp']
print(sorted(x, key=x.get))         # ['nyc', 'sf', 'boston', 'sgp']
print(sorted(x.items(), key=lambda x: x[1])) 
# [('nyc', 1), ('sf', 2), ('boston', 3), ('sgp', 4)]
print(sorted(x.items(), key=lambda x: x[0])) 
# [('boston', 3), ('nyc', 1), ('sf', 2), ('sgp', 4)]
print(sorted(x.items()))
# [('boston', 3), ('nyc', 1), ('sf', 2), ('sgp', 4)]

# =============================================================================
# Copy vs. Deepcopy for Python dictionaries
# =============================================================================

from copy import deepcopy

x = {'us': {'nyc': 1, 'sf': 2}, 'china': {'wuhan': 4}}
y = x.copy()

y['us']['sf'] += 100
print(y) # {'us': {'nyc': 1, 'sf': 102}, 'china': {'wuhan': 4}}
print(x) # {'us': {'nyc': 1, 'sf': 102}, 'china': {'wuhan': 4}}
y['china'] = {'hongkong': 5}
print(y) # {'us': {'nyc': 1, 'sf': 102}, 'china': {'hongkong': 5}}
print(x) # {'us': {'nyc': 1, 'sf': 102}, 'china': {'wuhan': 4}}

print("`deepcopy` example:")
x = {'us': {'nyc': 1, 'sf': 2}, 'china': {'wuhan': 4}}
z = deepcopy(x)
z['us']['sf'] += 100
print(z)
print(x)

# =============================================================================
# Counter vs. Dictionary
# =============================================================================

from collections import Counter
x = {'us': {'nyc': 1, 'sf': 2}, 'china': {'wuhan': 4}}
y = Counter(x)
print(x, y)
