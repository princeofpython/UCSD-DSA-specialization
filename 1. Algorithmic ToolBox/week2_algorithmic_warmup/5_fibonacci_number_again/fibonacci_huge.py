# Uses python3
import sys
def get_fibonacci_huge_naive(n, m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current % m
def get_fibonacci_mod_m(n,m):
    if n <= 1:
        return n

    previous = 0
    current  = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current)%m

    return current
def pisano_period(m):
    previous=0
    current=1
    for i in range(m*m):
        previous, current = current, (previous + current)%m
        if previous==0 and current==1:
            return (i+1)
def get_fibonacci_huge_fast(n,m):
    return get_fibonacci_mod_m(n%(pisano_period(m)),m)
if __name__ == '__main__':
    input = sys.stdin.read();
    n, m = map(int, input.split())
    print(get_fibonacci_huge_fast(n, m))
