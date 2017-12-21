# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 14:21:08 2017

@author: harrisot
"""

def generate_prime_numbers():
  """Generate a list of 26 prime numbers, each representing
  a character in the English alphabet"""
  
  primes  = []
  curr = 2
  while len(primes) < 26:
    ptest    = [curr for i in primes if curr%i == 0]
    primes  += [] if ptest else [curr]
    curr += 1
  return primes

def calculate_product(word, primes):
  """Given an English word, calculate the product of its 
  letters' corresponding prime numbers"""
  
  product = 1
  for ch in word: 
    if ch.isalpha():
      prime_index = ord(ch.lower())-97
      product *= primes[prime_index]
  return product

def search_word(vocab, plate):
  """Search the shortest word in the vocab that contains
  all the letters in the license plate"""
  primes = generate_prime_numbers()
  
  plate_product = calculate_product(plate, primes) 
  shortest = None
  
  for word in vocab:
    word_product = calculate_product(list(word), primes)
    if word_product%plate_product == 0:
      if shortest is None:
        shortest = word
      if len(shortest) > len(word):
        shortest = word
        
  return shortest

vocab = ['enjoy','enjoying', 'joy','joyful','joyous','joyousness']
plate = 'NY10NJ'

print(search_word(vocab, plate))