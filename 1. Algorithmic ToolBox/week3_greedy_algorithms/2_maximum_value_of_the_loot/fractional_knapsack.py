# Uses python3
import sys

def get_optimal_value(capacity, weights, values):
    value = 0.
    # write your code here
    val=[]
    n=len(weights)
    for i in range(n):
        val.append((values[i]/weights[i],weights[i]))
    val.sort()
    val.reverse()
    i=0
    while(capacity>0 and i<n):
        if capacity>val[i][1]:
            value+=val[i][0]*val[i][1]
            capacity-=val[i][1]
        else:
            value+=val[i][0]*capacity
            capacity=0
        i+=1
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.4f}".format(opt_value))
#3 50 60 20 100 50 120 30