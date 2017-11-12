#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 21:57:54 2017

@author: tz
"""
def prime_factors(n):
   div = 2
   factors = {}
   while n>1:
       if n % div == 0:
           factors[div] = factors.get(div, 0) + 1
           n = n // div
       else:
           div += 1
   return factors

print(prime_factors(8))


def prime_factorization(x):
  primes = []
  i = 2
  while i*i <= x:
    if x%i:
      i += 1
    else:
      x /= i
      primes.append(i)
  if x > 1:
    primes.append(int(x))
    
  return primes
  
print(prime_factorization(16))