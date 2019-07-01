# Uses python3
import sys

def fibonacci_sum_naive(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1
    sum      = 1

    for _ in range(n - 1):
        previous, current = current, previous + current
        sum += current

    return sum % 10
def pisano_period(m):
    previous=0
    current=1
    for i in range(m*m):
        previous, current = current, (previous + current)%m
        if previous==0 and current==1:
            return (i+1)
def fibonacci_sum_last_digit_fast(n):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (1+previous + current)%10

    return current

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    period=pisano_period(10)
    sum_over_period=fibonacci_sum_last_digit_fast(period)
    print((fibonacci_sum_last_digit_fast(n%period)+(sum_over_period*(n//period))%10)%10)
