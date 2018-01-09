# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:42:45 2017

@author: harrisot
"""

from functools import reduce

def update_state(v, ch, primes):
  """Helper function to divide v by ch's corresponding prime 
  value, to be returned as the value for key='*' """
  ch = primes[ord(ch)-97]
  return v//ch if v % ch==0 else v


def check_word(state_nested, word, primes):
  """Updates the nested dictionary when a new word comes in"""
  state = state_nested
  
  for ch in word: 
    try: 
      letter=[key for key in state if key!='*'][0]
    except:
      letter=None
  
    if ch not in state: 
      if letter:
        state.pop(letter)
      new_state = update_state(state['*'], ch, primes)
      state.update({ch: {'*': new_state}})
      
    state = state[ch]

  return state_nested, state


def search_word(vocab, plate):
  """Finds the shortest word in vocab, which contains all the
  letters in the license plate string"""
  
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
            47, 53, 59, 61, 67, 71, 79, 83, 89, 97, 101, 103]
  
  shortest = None
  
  plate_value = reduce(lambda a,b: a*b, 
                       [primes[ord(ch.lower())-97] for ch in plate if ch.isalpha()])
  
  state_nested = {'*': plate_value}
  
  for word in vocab:
    state_nested, state = check_word(state_nested, word, primes)
    
    print(state_nested)
    
    if state['*']==1:
      if shortest is None or \
         len(shortest) > len(word):
        shortest = word
        
  return shortest

vocab = ['enjoy','enjoying', 'joy','joyful','joyous','joyousness']
plate = 'NY10NJ'

plate = "1s3 PSt"
vocab = ["step","stepple","steps","stripe"] # vocab is sorted

print(search_word(vocab, plate))