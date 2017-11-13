# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 16:25:21 2017

@author: harrisot
"""

def prime_factors(n):
    primes = []
    i = 2
    rem = n
    
    while i*i < n:
        if rem%i == 0:
            primes.append(i)
            rem = rem // i
        else:
            i += 1
    if rem > 1:
        primes.append(rem)
    
    prime_map = dict()
    
    for i in primes: 
        if i not in prime_map.keys():
            prime_map.update({i: 1})
        else:
            prime_map[i] += 1
           
    return prime_map

def least_common_multiplier(ints):
    ans_map = {}
    for i in ints:
        prime_map = prime_factors(i)
        for j in prime_map.keys():
            if j not in ans_map.keys():
                ans_map.update({j:prime_map.get(j)})
            else:
                ans_map.update({j:max(ans_map.get(j), prime_map.get(j))})       
    ans = 1
    
    for i in ans_map.keys():
        ans *= (i*ans_map.get(i))
    return ans

ints = [10, 15, 6]
print("Prime factors for {}: {}".format(100, prime_factors(100)))

print("Least common multiplier for {}: {}".format(ints, least_common_multiplier(ints)))