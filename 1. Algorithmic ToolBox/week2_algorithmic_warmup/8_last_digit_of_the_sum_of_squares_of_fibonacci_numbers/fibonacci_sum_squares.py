# Uses python3
from sys import stdin

def fibonacci_sum_squares_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current * current

    return sum % 10
def get_fibonacci_mod_m(n,m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%m

    return current
def get_fibonacci_huge_fast(n,m):
    return get_fibonacci_mod_m(n%(pisano_period(m)),m)
def pisano_period(m):
    previous=0
    current=1
    for i in range(m*m):
        previous, current = current, (previous + current)%m
        if previous==0 and current==1:
            return (i+1)
if __name__ == '__main__':
    n = int(input())
    print((get_fibonacci_huge_fast(n, 10)*get_fibonacci_huge_fast(n+1, 10))%10)
