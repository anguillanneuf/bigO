# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 14:37:59 2017

@author: harrisot

What is a closure? 
A closure is an inner function that has access to the variables 
in the local scope where it is being created, even after the 
outer function has finished executing. 
"""

def outer_func(name):
  name_copy = name
  def inner_func():
    print("Hello "+name+"! Hello "+name_copy+"!")
    
  return inner_func

rabbit_func = outer_func("Judy Hopps")
rabbit_func() # prints "Hello Judy Hopps! Hello Judy Hopps!"

fox_func = outer_func("Nick Wilde")
fox_func() # print "Hello Nick Wilde! Hello Nick Wilde!"