# Uses python3
import numpy as np
def calc_fib(n):
    if n==0:
        return 0
    arr=np.zeros((n+1,),dtype=int)
    arr[1]=1
    for i in range(2,n+1):
        arr[i]=arr[i-1]+arr[i-2]
    return arr[n]

n = int(input())
print(calc_fib(n))
