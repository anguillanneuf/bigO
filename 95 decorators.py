# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:21:58 2017

@author: harrisot

Python Decorators
Python decorators are useful for extending the functionalities 
of functions, which you don't necessarily want to modify. 
They can be thought of as wrappers.
"""

from functools import wraps

def gen_html(func):
  @wraps(func)
  def gen_math(*x):
    return "Applying some math using function \"{2}\" on {0} gives us {1}.".format(x,func(*x),func.__name__)
  return gen_math

def cube(*args): 
  result = []
  for i in args:
    result.append(i*i*i)
  return result

f = gen_html(cube)
print(f.__name__)
print(f(1,2,3))

@gen_html
def prime_factors(x):
  primes = []
  q = 2
  while q*q < x: 
    if x%q == 0: 
      x = x/q
      primes.append(int(q))
      continue
    q+= 1
  if x>1:
    primes.append(int(x))
  return primes

print(prime_factors(1985))


