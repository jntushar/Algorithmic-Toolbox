# Uses python3
import sys


def get_fibonacci_huge_naive(n, m):
    current, previous = 1, 0

    for i in range(m * m + 1):
        previous, current = current, (current + previous) % m
        if (previous, current) == (0, 1):
            time_period = i + 1
            break

    index = n % time_period
    if index < 1:
        return index
    previous, current = 0, 1
    for i in range(2, index + 1):
        previous, current = current, (current + previous) % m
    return current


if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_naive(n, m))
