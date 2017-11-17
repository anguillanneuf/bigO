# -*- coding: utf-8 -*-
"""
Created on Fri Nov 17 13:39:38 2017

@author: harrisot

abcbc
a.*bc

[a,a]
[ab, a.*] ''
[ab, a.*b] ''+'b'
[abc, a.*bc]
[abcb, a.*bc_] Fail!

[ab, a.*] 'b'
[abc, a.*b] Fail!

[abc, a.*] 'bc'
[abcb, a.*b]
[abcbc, a.*bc] 
[abcbc_, a.*bc_] pass!

"""

def is_match(text, pattern):
  text_len = len(text)
  pattern_len = len(pattern)
  text_ptr = 0
  pattern_ptr = 0
  
  while text_ptr < text_len:
    if len(pattern) == 1 and len(text) > 1:
      return False
    if pattern_ptr+1 >= pattern_len and text_ptr +1 == text_len:
      return True
    if pattern_ptr+1 >= pattern_len:
      return False
    
    if pattern[pattern_ptr+1] == "*":
      # .*
      if pattern[pattern_ptr] == ".":
        if pattern_ptr+2 == pattern_len: 
          return True
        else:
          # need recursion instead - test all possible scenarios
          letter = pattern[pattern_ptr+2]
          while text[text_ptr] != letter:
            text_ptr += 1
            if text_ptr >= text_len: break
          pattern_ptr += 2
      # [a-z0-9]*
      else:
        while text[text_ptr] == pattern[pattern_ptr]:
          text_ptr += 1
          if text_ptr >= text_len: break
        pattern_ptr += 2
    elif pattern[pattern_ptr] == "." or pattern[pattern_ptr] == text[text_ptr]:
      text_ptr += 1
      pattern_ptr += 1
    else:
      return False
  return True

print(is_match("aa", "a"))
print(is_match("aa", "aa"))
print(is_match("abc", "a.c"))
print(is_match("abbb", "ab*"))
print(is_match("abbbbbf", "ab.*f"))
print(is_match("abaa", "a.*a*"))
print(is_match("abbdbb", "ab*d"))
# really tricky!
print(is_match("abcbc", ".*bc"))