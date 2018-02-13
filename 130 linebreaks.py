#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 12 22:08:49 2018

@author: tz

"Given a string of English text and a paragraph width, 
design an algorithm to break the texts into lines not 
exceeding the paragraph width, and not too jagged."
"""

class Lines(object):
  
    def __init__(self, raw=""):
        self.raw        = raw
        self.words      = self.raw.split()
        self.wordlens   = [len(w) for w in self.raw.split()]
    
    def split_text_into_lines(self, width=80):
        n   = len(self.wordlens)
        mem = [[float('inf') for _ in range(n)] for _ in range(n)]
        
        for i in range(n):            
            for j in range(i,n):
                l = sum(self.wordlens[i:j+1])+(j-i)
                if width - l >= 0: 
                    cost  = (width - l) ** 2
                    mem[i][j] = cost
                else:
                    break
                
#        print("Loop up matrix for cost: ")
#        for row in mem: print(row)
        
        C   = [None for _ in range(n)]
        P   = [None for _ in range(n)]

        for i in range(n-1, -1, -1):
            cost = float('inf')
            for j in range(n-1, i-1, -1):
                if mem[i][j] == float('inf'): 
                    continue
                else:
                    left = mem[i][j]
                    right = 0 if j==n-1 else C[j+1]
                    temp_cost = left + right
                    if temp_cost < cost:
                        cost = temp_cost
                        C[i] = cost
                        P[i] = j+1
        
        print("\nMinimum cost: {}".format(C[0]))
        
        last = 0
        curr = 0
        while curr < len(P):
            line = ' '.join(self.words[last:curr])
            print(line)
            last = curr
            curr = P[curr]
        if last != len(P):
            print(' '.join(self.words[last:]))
        
        

raw = "Try this: Given a string of English text and a paragraph width, design an algorithm to break the texts into lines not exceeding the paragraph width, and not too jagged."
lines = Lines(raw)
lines.split_text_into_lines(30)
    

