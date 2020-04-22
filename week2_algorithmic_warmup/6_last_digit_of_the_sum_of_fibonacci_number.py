import sys

def fibonacci_sum_naive(n):
    index = n%60
    if index < 1:
        return index
    prev, curr = 0, 1
    sum1 = 1
    for i in range(2, index + 1):
        prev, curr = curr, (curr + prev) % 10
        sum1 = (sum1 + curr) % 10
    return sum1


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    print(fibonacci_sum_naive(n))
