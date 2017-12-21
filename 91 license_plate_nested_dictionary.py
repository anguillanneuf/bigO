# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 11:39:34 2017

@author: harrisot
"""

def create_dict(plate):
  """Creates a dictionary of characters and character 
  counts as key-value pairs from an input string"""
  
  plate_dict = dict()
  
  for ch in plate:
    ch = ch.lower()
    if ch.isalpha():
      if ch not in plate_dict.keys():
        plate_dict.update({ch: 1})
      else:
        plate_dict[ch] += 1
  return plate_dict

def update_state(plate_state, ch):
  """Updates the corresponding character count in a dictionary
  of characters and character counts as key-value pairs"""
  
  plate_state_copy = plate_state.copy()
  
  if ch in plate_state_copy.keys():
    plate_state_copy[ch] -= 1
  return plate_state_copy

def check_word(state_nested, word):
  """Updates the nested dictionary when a new word comes in"""
  
  state = state_nested
  
  for ch in word: 
    letters = [key for key in state.keys() if key!='*']
    
    if len(letters) > 0:
      letter = letters[0]
    
    if ch not in state.keys(): 
      if len(letters) > 0:
        state.pop(letter)
      state.update({ch: {'*': update_state(state['*'], ch)}})

    state = state[ch]
    
  return state_nested, state

def search_word(vocab, plate):
  """Searches for the shortest word in a list of words that 
  contains all the letters in the plate string"""
  
  shortest = None
  plate_dict = create_dict(plate)
  state_nested = {'*': plate_dict}
  
  for word in vocab:

    state_nested, state = check_word(state_nested, word)

    if not any(v > 0 for v in state['*'].values()):
      if shortest is None:
        shortest = word
      elif len(shortest) > len(word):
        shortest = word
  return shortest

vocab = ['enjoy','enjoying', 'joy','joyful','joyous','joyousness']
plate = 'NY10NJ'

print(search_word(vocab, plate))