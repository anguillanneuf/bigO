'''
Find all the permutations of a string with no duplicated letters

'''
      
def permutation(s, prefix=None):
  
  if len(s)==0:
    print(prefix)
    
  else:
    for i in range(len(s)):
      rem = s[:i]+s[i+1:]
      permutation(rem, prefix+s[i])

permutation("cat", prefix="")

'''Print:
cat
cta
act
atc
tca
tac
'''