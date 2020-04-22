import sys


def gcd_naive(a, b):
    if b == 0:
        return a
    reminder = a % b
    return gcd_naive(b, reminder)


if __name__ == "__main__":
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(gcd_naive(a, b))
