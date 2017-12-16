#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 16:28:11 2017

@author: tz
"""
def helper(p,q,prefix,n):
  if p==q==3:
    print(prefix)

  if p>=q and p<=n:
    helper(p+1,q,prefix+'(',n)
    helper(p,q+1,prefix+')',n)

def parens(n):
  p = q = 0
  helper(p,q,'',n)

parens(3)