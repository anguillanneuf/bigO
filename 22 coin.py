#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 11 17:37:31 2017

@author: tz

input
---
amount = 4
denominations = [1,2,3]

output
---
number of ways = 4

 0  1  2  3  4
[0, 0, 0, 0, 0]

coint = 1
range(1,5)
[1, 0, 0, 0, 0]
[1, 1, 0, 0, 0]
[1, 1, 1, 0, 0]
[1, 1, 1, 1, 0]
[1, 1, 1, 1, 1]

coin = 2
range(2,5)
l[2] += l[0]
[1, 1, 2, 1, 1]
l[3] += l[1]
[1, 1, 2, 2, 1]
l[4] += l[2]
[1, 1, 2, 2, 3]

coin = 3
range(3,5)
l[3] += l[0]
[1, 1, 2, 3, 3]
l[4] += l[1]
[1, 1, 2, 3, 4]


"""


def change_possibilities_bottom_up(amount, denominations):
    ways_of_doing_n_cents = [0] * (amount + 1)
    ways_of_doing_n_cents[0] = 1
    #print(ways_of_doing_n_cents)

    for coin in denominations:

        for higher_amount in range(coin, amount + 1):
            
            higher_amount_remainder = higher_amount - coin
            ways_of_doing_n_cents[higher_amount] += \
                ways_of_doing_n_cents[higher_amount_remainder]
            #print(ways_of_doing_n_cents)

    
    return ways_of_doing_n_cents[amount]

print(change_possibilities_bottom_up(8, [1,2,3]))

def coins(amount, c):
    # top down recursion
    global cnt
    cnt = 0
    
    def _coins(rem, i, c):
        global cnt
        if rem == 0:
            cnt+=1
            return # return is a formal exit
        
        if i <= len(c)-1:
            K = rem//c[i]
            for k in range(K, -1, -1):
                _coins(rem-k*c[i], i+1, c)
                
    _coins(amount, 0, c)
    
    return cnt


def coins_it(amount, c):
    # bottom up iterative
    mem = [0 for _ in range(amount+1)]
    
    for v in sorted(c):
        
        for u in range(v, amount+1):
            if u == v:
                mem[v] += 1
            else:
                mem[u] += mem[u-v]
    
    return mem[amount]

print(coins(10, [5,2,1]))
print(coins_it(10, [5,2,1]))



