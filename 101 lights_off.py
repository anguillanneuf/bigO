# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 15:32:51 2018

@author: harrisot
"""
import random

class LightsOff(object):
  def __init__(self, n):
    self.board = [[0 for i in range(n)] for j in range(n)]
    self.n = n
    
  def push_a_button(self,i,j):
    if i-1>=0:
      self.board[i-1][j] ^= 1
    if j-1>=0:
      self.board[i][j-1] ^= 1
    if i+1< self.n:
      self.board[i+1][j] ^= 1
    if j+1< self.n:
      self.board[i][j+1] ^= 1
    
    self.board[i][j] ^= 1
  
  @property
  def game_finish(self):
    for i in range(self.n):
      for j in range(self.n):
        if self.board[i][j]>0:
          return False
    return True
    
  def init_game(self, level = 1):
    while level > 0 or self.game_finish:
      i = random.randint(0,self.n-1)
      j = random.randint(0,self.n-1)
      self.push_a_button(i,j)
      level -= 1
      

      
game1 = LightsOff(3)
mylevel = 2
game1.init_game(level=mylevel)
print("New Level {} Game".format(mylevel))
for row in game1.board: print(row)