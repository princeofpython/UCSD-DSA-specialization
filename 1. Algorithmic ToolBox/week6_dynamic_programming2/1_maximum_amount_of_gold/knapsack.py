# Uses python3
import sys
import numpy
def optimal_weight(W, w, n):
    weights=numpy.zeros((W+1,n+1),dtype=int)
    for j in range(1,n+1):
        for weight in range(1,W+1):
            listt=[weights[weight,j-1]]
            if w[j-1]<=weight:
                listt.append(weights[weight-w[j-1],j-1]+w[j-1])
            weights[weight,j]=max(listt)
    return(weights[W,n])

if __name__ == '__main__':
    input = sys.stdin.read()
    W, n, *w = list(map(int, input.split()))
    print(optimal_weight(W, w, n))
