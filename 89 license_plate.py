# -*- coding: utf-8 -*-
"""
Created on Wed Dec 20 13:44:16 2017

@author: harrisot
"""

def create_dict(plate):
  plate_dict = dict()
  
  for ch in plate:
    ch = ch.lower()
    if ch.isalpha():
      if ch not in plate_dict.keys():
        plate_dict.update({ch: 1})
      else:
        plate_dict[ch] += 1
        
  return plate_dict


def search_brute_force(vocab, plate):
  plate_dict = create_dict(plate)
  shortest = None
  
  for word in vocab: 
    word_dict = create_dict(word)
    
    for key in plate_dict.keys():
      if key in word_dict.keys(): 
        word_dict[key] -= plate_dict[key]
        if word_dict[key] < 0:
          continue
      else: 
        continue
    
    if sum([True for v in word_dict.values() if v < 0]) > 0:
      if shortest is None:
        shortest = word
      elif len(shortest) > len(word):
        shortest = word    
          
  return shortest

def search_prefix(vocab, plate):
  return None

vocab = ['enjoy','enjoying', 'joy','joyful','joyous','joyousness']
plate = 'NY10NJ'

print(search_brute_force(vocab, plate))
print(search_prefix(vocab, plate))