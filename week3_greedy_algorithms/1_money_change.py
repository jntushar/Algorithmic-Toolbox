import sys


def get_change(m):
    coins = [10, 5, 1]
    no_of_coins = 0
    i = 0
    while m > 0:
        if m - coins[i] >= 0:
            m -= coins[i]
            no_of_coins += 1
        else:
            i += 1
    return no_of_coins


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
