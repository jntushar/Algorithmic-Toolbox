def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    num1 = max(numbers)
    numbers.pop(numbers.index(num1))
    num2 = max(numbers)
    max_product = num1 * num2
    return max_product


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
