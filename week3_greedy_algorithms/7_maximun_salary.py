import sys


def greater(digit, max_digit):
    return digit + max_digit > max_digit + digit


def largest_number(a):
    res = ""
    while a:
        max_digit = '0'
        for i in a:
            if greater(i, max_digit):
                max_digit = i
        res += max_digit
        a.remove(max_digit)
    return res


if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    a = data[1:]
    print(largest_number(a))
    
