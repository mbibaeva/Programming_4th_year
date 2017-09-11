
def fibonacci(n):
    mem = {0: 1, 1: 1}
    if n < 0 or type(n) is float:
        return
    if n not in mem:
        mem[n] = fibonacci(n-1) + fibonacci(n-2)
    return mem[n]
