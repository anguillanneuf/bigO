# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:56:55 2017

@author: harrisot
"""
class Trie:
  def __init__(self):
    self.root = {'~': {}}
    self.word_cloud = {}
    
  def expand(self, word):
    curr = self.root.get('~')
    
    for w in word:
      if w not in curr:
        curr[w] = {}
      curr = curr[w]
      
    if '*' not in curr:
      curr['*'] = 1
      self.word_cloud.update({word: 1})
    else:
      curr['*'] += 1
      self.word_cloud[word] += 1

def word_cloud(s):

  wordTree = Trie()
  i = None
  j = None
  
  for ptr,c in enumerate(s):
    if ord(c) >= ord('A') and ord(c) <= ord('z'):
      if i is None:
        i = ptr
      else:
        j = ptr
    else:
      if i is not None and j is not None:
        wordTree.expand(s[i:j+1].lower())
      i = None
      j = None

  
  return wordTree.word_cloud

s1 = 'After beating the eggs, Dana read the next step:'
s2 = 'Add milk and eggs, then add flour and sugar.'

print(word_cloud(s1))
print(word_cloud(s2))