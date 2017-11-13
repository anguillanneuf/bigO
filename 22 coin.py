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



