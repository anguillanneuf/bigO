def allFib(n):
    mem = [0 for i in range(n)]
    for i in range(n):
        print('{}'.format(fib_internal(i, mem)))
    print(mem)


def fib_internal(n, mem):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif mem[n] > 0:
        return mem[n]  # commenting this line results in +0.03 seconds in compute time

    mem[n] = fib_internal(n - 1, mem) + fib_internal(n - 2, mem)
    return mem[n]


allFib(10)