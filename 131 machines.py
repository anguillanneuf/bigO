#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 13 16:48:25 2018

@author: tz
"""

from collections import Counter

def find_max_output(G):
    
    # Step 1: candidates for final machine
    
    candidates = set(G['machines'].keys())
    for machine in G['machines']:        
        if not any(e.find('m') >=0 for e in G['machines'][machine]['input']):
            candidates.remove(machine)
    candidates = list(candidates)
    
    # Step 2: search for final machine in candidates queue
    
    while candidates:
        candidate = candidates.pop(0)
        ms = [e for e in G['machines'][candidate]['input'] if e.find('m') >= 0] 
        c = len(ms)
        
        for m in ms:            
            if m not in candidates:
                c -= 1
                mv = G['machines'][candidate]['input'][m]
                G['machines'][candidate]['input'].pop(m)
                G_t1 = Counter(G['machines'][candidate]['input'])
                G_t2 = Counter(G['machines'][m]['input'])
    
                for _ in range(mv):
                    G_t1 += G_t2
            
                G['machines'][candidate]['input'] = dict(G_t1)
        print(candidate, c)           
        if c > 0:
            candidates.append(candidate)
            
    temp = []
    for source in G['machines'][candidate]['input']:
        temp.append(G['sources'][source] // G['machines'][candidate]['input'][source])
        
    return max(0, min(temp))         


G = {'sources': {'s1': 90, 's2': 130, 's3': 110}, 
     'machines': {'m1': {'input': {'s1': 4, 's2': 2}, 'output': 1},
                  'm2': {'input': {'s3': 5, 'm4': 2}, 'output': 1},
                  'm3': {'input': {'m1': 1, 'm2': 2, 's2': 5}, 'output': 1},
                  'm4': {'input': {'s2': 1}, 'output': 1}}}


print(find_max_output(G))