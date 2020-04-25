import sys


def get_optimal_value(capacity, weights, values, n):
    value = 0.
    valuePerItem = []
    for i in range(n):
        valuePerItem.append(values[i]/weights[i])

    for i in range(n):
        if capacity == 0:
            return value

        max_valuePerItem = max(valuePerItem)
        index_of_max_valuePerItem = valuePerItem.index(max_valuePerItem)
        valuePerItem[index_of_max_valuePerItem] = -1
        a = min(capacity, weights[index_of_max_valuePerItem])
        value += a * max_valuePerItem
        weights[index_of_max_valuePerItem] -= a
        capacity -= a

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values, n)
    print("{:.10f}".format(opt_value))
