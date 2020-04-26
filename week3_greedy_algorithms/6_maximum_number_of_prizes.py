import sys


def optimal_summands(n):
    summands = []
    prize = 1
    sum_of_summands = 0

    while sum_of_summands <= n:
        if (sum_of_summands + prize) <= n:
            summands.append(prize)
            sum_of_summands += prize
        else:
            summands[-1] += n - sum_of_summands
            break
        prize = prize + 1

    return summands


if __name__ == '__main__':
    input = sys.stdin.read()
    n = int(input)
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
