# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 16:56:55 2017

@author: harrisot
"""

class Trie:
  def __init__(self):
    self.root = {'~': {}}
    self.word_cloud = {}
    self.lastCh = False
    self.toAddWord = False
    
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
  """O(n) time"""
  
  wordTree = Trie()
  i = None
  j = None
  
  for ptr,c in enumerate(s):
    
    if (ord(c) >= ord('A') and ord(c) <= ord('z')) or \
    ((ord(c)==ord('-') or ord(c)==ord('\'')) and wordTree.lastCh):
      if i is None:
        i = ptr
        wordTree.lastCh = True
      else:
        j = ptr
        if j == len(s)-1: 
          wordTree.toAddWord = True
    else:
      if i is not None and j is not None:
        wordTree.toAddWord = True
        
    if wordTree.toAddWord:
      wordTree.expand(s[i:j+1].lower())
      wordTree.toAddWord = False
      i = None
      j = None
      wordTree.lastCh = False

  return wordTree.word_cloud

s1 = 'After beating the eggs, Dana read the next step:'
s2 = 'Add milk and eggs, then add flour and sugar.'
s3 = 'We came, we saw, we conquered...then we ate Bill\'s (Mille-Feuille) cake.'
s4 = 'The bill came to five dollars.'
s5 = 'ronny\'s ronny\'s ronny\'s tianzi'
print(word_cloud(s1))
print(word_cloud(s2))
print(word_cloud(s3))
print(word_cloud(s4))
print(word_cloud(s5))