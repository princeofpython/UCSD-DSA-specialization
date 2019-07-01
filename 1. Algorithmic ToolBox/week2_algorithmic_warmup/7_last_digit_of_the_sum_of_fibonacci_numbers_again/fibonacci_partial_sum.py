# Uses python3
import sys

def fibonacci_partial_sum_naive(from_, to):
    sum = 0

    current = 0
    next  = 1

    for i in range(to + 1):
        if i >= from_:
            sum += current

        current, next = next, current + next

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
    period=pisano_period(10)
    sum_over_period=fibonacci_sum_last_digit_fast(period)
    #input = sys.stdin.read();
    m, n = map(int, input().split())
    print(((fibonacci_sum_last_digit_fast(n%period)+(sum_over_period*(n//period))%10)-(fibonacci_sum_last_digit_fast((m-1)%period)+(sum_over_period*((m-1)//period))%10))%10)
    #num_periods