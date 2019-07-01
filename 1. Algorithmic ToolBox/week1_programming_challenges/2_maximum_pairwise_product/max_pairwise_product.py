# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product
def max_pairwise_product_fast(numbers):
    n=len(numbers)
    fir=0
    sec=0
    for first in range(n):
        if fir<numbers[first]:
            fir=numbers[first]
            max_index=first
    for second in range(n):
        if sec<numbers[second] and second!=max_index:
            sec=numbers[second]
    return fir*sec

if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))
