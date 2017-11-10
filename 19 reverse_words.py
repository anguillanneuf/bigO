arr = [ 'p', 'e', 'r', 'f', 'e', 'c', 't', '  ',
                'm', 'a', 'k', 'e', 's', '  ',
                'p', 'r', 'a', 'c', 't', 'i', 'c', 'e' ]

def reverse(x, i, j):
  while i < j:
    x[i], x[j] = x[j], x[i]
    i += 1
    j -= 1
  return x

def reverse_words(x):
  x = reverse(x, 0, len(x)-1)
  start = 0
  i = 0
  
  for i,v in enumerate(x):
    if v.isspace():
      x = reverse(x, start, i-1)
      start = i + 1
    if i == len(x)-1:
      x = reverse(x, start, i)
  return x

print(reverse_words(arr))