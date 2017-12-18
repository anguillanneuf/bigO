# python lists are mutable
mem1 = ['a', 'b', 'c']

# python global vars are mutable
global mem2
mem2 = 'a'

# python class properties are also mutable
class Params():
  mem3 = 'a'


def hello(m1, p):
    
    m1[1] = 'alien'   # modifies mem1
    
    global mem2
    mem2 = 'alien'    # modifies mem2 without calling mem2 as a param
    
    p.mem3 += 'alien' # modifies p.mem3
    

print(mem1)
print(mem2)
p = Params()
print(p.mem3)

hello(mem1, p)

print(mem1)
print(mem2)
print(p.mem3)