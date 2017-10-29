mem1 = ['a', 'b', 'c']
global mem2
mem2 = 'a'

def hello(m1):
    global mem2
    m1[1] = 'alien'
    mem2 = 'alien'

print(mem1)
print(mem2)
hello(mem1)
print(mem1)
print(mem2)
