# -*- coding: utf-8 -*-
"""
Created on Wed Dec 27 13:59:29 2017

@author: harrisot

What is first-class function?
A programming language that has first-class functions treats
functions as its first-class citizens. 

What are first-class citizens?
A first-class citizen or object in a programming language is 
an entity that supports all the operations generally available 
to other entities. These operations typically include being 
passed as an argument(1), being returned from a function(2),  
and being assigned to a variable(3). 
 
"""

def cube(x):
  return x*x*x

def mymap(func, arr): 
  """(1)func is being passed as an argument"""
  result = []
  for i in arr:
    result.append(cube(i))
  return result

"""(3)mymap is being assigned to a variable"""
f = mymap 
print(mymap) # prints <function mymap at ...>
print(f)
print(f(cube, [1,2,3,4,5])) # prints [1,8,27,64,125]

def gen_html(tag):
  """(2)pass_content is being returned from a function"""
  def pass_content(content):
    print("<{0}>{1}</{0}>".format(tag, content))
  return pass_content

g_header = gen_html("h1")
print(g_header) # prints <function gen_html.<local>.pass_content at ...>
g_header("Nick Wilde and Judy Hopps") # prints <h1>Nick Wilde and Judy Hopps</h1>

