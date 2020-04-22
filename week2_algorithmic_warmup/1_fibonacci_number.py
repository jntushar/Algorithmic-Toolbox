def calc_fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a+b
    return a


n = int(input())
print(calc_fib(n))
