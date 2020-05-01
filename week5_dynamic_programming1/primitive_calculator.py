import sys
from math import inf


def optimal_sequence(n):
    min_operation = [0]*(n+1)

    sequence = []
    sequence.append([0])
    sequence.append([1])

    for i in range(2, n+1):
        temp3 = inf
        temp2 = inf

        if i % 3 == 0:
            temp3 = min_operation[int(i/3)] + 1
        if i % 2 == 0:
            temp2 = min_operation[int(i/2)] + 1
        temp1 = min_operation[i - 1] + 1

        min_value = min(temp1, temp2, temp3)
        min_operation[i] = min_value

        if min_value == temp1:
            sequence.append(sequence[i - 1] + [i])
            continue
        if min_value == temp2:
            sequence.append(sequence[int(i/2)] + [i])
            continue
        if min_value == temp3:
            sequence.append(sequence[int(i/3)] + [i])

    return sequence[-1]


input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')
