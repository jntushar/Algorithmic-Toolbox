import sys


def compute_min_refills(distance, tank, stops):
    number_of_refills = 0
    current_refill = 0
    last_refill = 0

    while stops[last_refill]+tank < distance:
        last_refill = current_refill
        while current_refill < len(stops) - 1 and stops[current_refill+1] <= stops[last_refill]+tank:
            current_refill += 1

        if current_refill == last_refill:
            return -1
        if stops[last_refill]+tank < distance:
            number_of_refills += 1

    return number_of_refills


if __name__ == '__main__':
    d, m, n, *stops = map(int, sys.stdin.read().split())
    stops.insert(0, 0)
    stops.append(d)
    print(compute_min_refills(d, m, stops))
