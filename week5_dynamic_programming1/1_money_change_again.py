import sys
from math import inf


def get_change(money):
    min_coins = [0]*(money+1)
    coins = [1, 3, 4]

    for m in range(1, money+1):
        min_coins[m] = inf
        for i in coins:
            if m >= i:
                num_coins = min_coins[m-i]+1
                if num_coins < min_coins[m]:
                    min_coins[m] = num_coins
    return min_coins[money]


if __name__ == '__main__':
    money = int(sys.stdin.read())
    print(get_change(money))
