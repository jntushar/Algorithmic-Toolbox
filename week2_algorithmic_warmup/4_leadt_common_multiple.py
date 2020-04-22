import sys

def gcd_naive(a, b):
    if b == 0:
        return a
    reminder = a % b
    return gcd_naive(b, reminder)


def lcm_naive(a, b):
    return int(a*b/gcd_naive(a, b))


if __name__ == '__main__':
    input = sys.stdin.read()
    a, b = map(int, input.split())
    print(lcm_naive(a, b))

