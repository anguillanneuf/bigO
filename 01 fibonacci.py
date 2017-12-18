def allFib(n):
    # O(2^n) time despite for loop: 2^1+2^2+2^3+..+2^n=2^(n+1)
    mem = [0 for i in range(n)]
    for i in range(n):
        print(fib_internal(i, mem))

def fib_internal(n, mem):
    if n <= 1:
        mem[n]=n
        return n
    elif mem[n] > 0:
        return mem[n]

    mem[n] = fib_internal(n - 1, mem) + fib_internal(n - 2, mem)
    return mem[n]

# Recursion with memory
allFib(10)



def get_fib(position):
    if position < 0:
        return -1
    elif position in [0,1]:
        return position
    else:
        return get_fib(position-1) + get_fib(position-2)
  
# Recursion without memory
print("Nth Fibonacci: {}".format(get_fib(10)))



def fib_binet(n):
    return int( 1/(5**0.5) * \
               (((1+5**0.5)/2)**n - ((1-5**0.5)/2)**n) )

# O(1) solution
print("Nth Fibonacci: {}".format(fib_binet(10)))