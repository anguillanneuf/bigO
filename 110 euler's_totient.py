#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 14:41:23 2018

@author: tz
"""

def prime_factorization(n):
    q = 2
    primes = set()
    
    while q*q <= n:
        if n%q == 0:
            primes.add(q)
            n /= q
        else:
            q+=1

    if n > q:
        primes.add(n)
        
    return primes

def eulers_totient(n):
    """Euler's totient of n means the numbers from [0,n] 
    that are relative primes to n"""
    
    # step 1: prime factorialization
    primes = prime_factorization(n)
    res = []
    cnt = 0
    
    # step 2: iterate 1 thru n
    for v in range(1,n):
        for p in primes:
            if v % p == 0:
                break
        else:
            res.append((v,n))
            cnt += 1
    return res, cnt

print(eulers_totient(6))