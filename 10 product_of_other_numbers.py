# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def get_products_of_all_ints_except_at_index(ints):
    products = []
    for i,v in enumerate(ints):
        temp = 1
        for j in ints:
            if j != v:
                temp *=j
        products.append(temp)
        
    return products

print(get_products_of_all_ints_except_at_index([1,2,3,4]))


def get_products_of_all_ints_except_at_index2(ints):
    products = [1]*len(ints)
    products1 = [1]*len(ints)
    products2 = [1]*len(ints)
    
    for i in range(1,len(ints)):
        products1[i] = products1[i-1]*ints[i-1]
        
    for i in range(-1, -len(ints)-1, -1):
        products2[i] = products2[i+1]*ints[i+1]
        
    for i in range(len(ints)):
        products[i] = products1[i]*products2[i]
        
    return products


def get_products_of_all_ints_except_at_index3(ints):
  
  products = [1] * len(ints)
  
  product = 1
  for i in range(len(ints)):
    products[i] = product
    product *= ints[i]
    
  product = 1
  for i in range(len(ints)-1, -1, -1):
    products[i] *= product
    product *= ints[i]
    
  return products
  


print(get_products_of_all_ints_except_at_index2([1,2,3,4]))
print(get_products_of_all_ints_except_at_index3([1,2,3,4]))

#==============================================================================
# Reflection:
# Write out the solution on paper, and look for patterns. 
# See if I can code the patterns. 
#==============================================================================
