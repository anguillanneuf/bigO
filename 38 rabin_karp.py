#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 21:39:50 2017

@author: tz

If text has length b, substring length s, the Rabin-Karp algorithm 
could do the search in O(b+s) time on average and O(bs) time in the
worst case. This is better than O(s(b-s)) if we search the substring
iteratively in text. 

d: number of chars in the alphabet
q: a prime number
h: d^(m-1)

hash(txt[n...n+m)]) = (d*(hash(txt[n...n+m-1]) - h*txt[n]) + txt[n+m])%q
"""

def rabin_karp_algo(text, substring):
    """suppose text is longer than substring, or n > m"""
    
    found = []
    
    n = len(text)
    m = len(substring)
    
    q = 101 # a prime number
    d = 128 # constant
    
    # Calculate pow(h, m-1)
    h = d**(m-1)%q
    # alternatively, this is really cool!
    h = 1
    for i in range(m-1):
        h = h*d % q
    
    # Calculate hash
    substring_hash = 0
    text_hash = 0
    
    for i in range(m):
        substring_hash = ( d*(substring_hash - h*0) + ord(substring[i]) ) % q
        text_hash      = ( d*(text_hash - h*0)      + ord(text[i])      ) % q
        
    
    for i in range(n-m+1):
        
        if substring_hash == text_hash: 
            for j in range(m):
                if text[i+j]!=substring[j]:
                    break
            else:
                found.append(i)
                print("Substring found at {}".format(i))
        
        if i < n - m:
            text_hash = ( d*(text_hash - h*ord(text[i])) + ord(text[i+m]) ) % q
            
            if text_hash < 0: 
                text_hash += q
    
    return found

print(rabin_karp_algo('Get bit; set bit; clear bit; update bit', 'bit'))