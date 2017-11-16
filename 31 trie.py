# -*- coding: utf-8 -*-
"""
Created on Thu Nov 16 11:40:01 2017

@author: harrisot

Implement trie
"""

class Trie:
    def __init__(self):
        self.root_node = {'~': {}}
        
    def expand(self, word):
        is_new_word = False
        curr = self.root_node.get('~')
        
        for w in word:
            if w not in curr:
                is_new_word = True
                curr[w] = {}
            curr = curr[w]
            
        if '*' not in curr:
            is_new_word = True
            curr['*'] = {}
            
        if is_new_word:
            print('Added "{}"...'.format(word))
        else:
            print('"{}" has been added before...'.format(word))
            
        return is_new_word
    
t = Trie()
t.expand('tia')
t.expand('tia')
t.expand('ron')
t.expand('tianzi')
t.expand('ronny.rest')
print(t.root_node)

