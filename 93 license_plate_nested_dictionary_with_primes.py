# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 16:42:45 2017

@author: harrisot
"""

def update_state(v, ch, primes):
  """Helper function to divide v by ch's corresponding prime 
  value"""
  ch = primes[ord(ch)-97]
  return v//ch if v % ch==0 else v


def check_word(state_nested, word, primes):
  """Updates the nested dictionary when a new word comes in"""
  state = state_nested
  
  for ch in word: 
    letters = [key for key in state.keys() if key!='*']
    if letters:
      letter = letters[0]
      
    if ch not in state.keys(): 
      if letters:
        state.pop(letter)
      new_state = update_state(state['*'], ch, primes)
      state.update({ch: {'*': new_state}})
    state = state[ch]

  return state_nested, state


def calculate_product(word, primes):
  product = 1
  for ch in word: 
    if ch.isalpha():
      product *= primes[ord(ch.lower())-97]
  return product


def search_word(vocab, plate):
  """Finds the shortest word in vocab, which contains all the
  letters in the license plate string"""
  
  primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
            47, 53, 59, 61, 67, 71, 79, 83, 89, 97, 101, 103]
  shortest = None
  plate_value = calculate_product(plate, primes)
  state_nested = {'*': plate_value}
  
  for word in vocab:
    state_nested, state = check_word(state_nested, word, primes)

    if state['*']==1:
      if shortest is None or \
         len(shortest) > len(word):
        shortest = word
  return shortest

vocab = ['enjoy','enjoying', 'joy','joyful','joyous','joyousness']
plate = 'NY10NJ'

print(search_word(vocab, plate))