# -*- coding: utf-8 -*-
"""
Created on Fri Nov 10 17:18:21 2017

@author: harrisot
"""
# My implementation: (2n, n)/(n+1)
def catalan(n):
    temp = 1
    for i in range(1,n+1):
        temp *= (n+i)
        temp /= i
    return int(temp/(n+1))

for i in range(10):
    print(catalan(i))


# II: A recursive function to find nth catalan number
def catalan(n):
    # Base Case
    if n <=1 :
        return 1
 
    # Catalan(n) is the sum of catalan(i)*catalan(n-i-1)
    res = 0
    for i in range(n):
        res += catalan(i) * catalan(n-i-1)
 
    return res
 
# Driver Program to test above function
for i in range(10):
    print(catalan(i))
    

    
# III: Returns value of Binomial Coefficient C(n, k)
    
def binomialCoefficient(n, k):
    # since C(n, k) = C(n, n - k)
    if (k > n - k):
        k = n - k
 
    # initialize result
    res = 1
 
    # Calculate value of [n * (n-1) *---* (n-k + 1)]
    # / [k * (k-1) *----* 1]
    for i in range(k):
        res = res * (n - i)
        res = res / (i + 1)
    return res
 
# A Binomial coefficient based function to
# find nth catalan number in O(n) time
def catalan(n):
    c = binomialCoefficient(2*n, n)
    return c/(n + 1)
 
for i in range (11):
    print (catalan(i))
 
