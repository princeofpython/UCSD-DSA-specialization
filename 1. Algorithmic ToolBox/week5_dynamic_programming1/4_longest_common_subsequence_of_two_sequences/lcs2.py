#Uses python3

import sys
import numpy
def lcs2(a, b):
    #write your code here
    m=len(a)
    n=len(b)
    D=numpy.zeros((m+1,n+1),dtype=int)
    for j in range(1,n+1):
        for i in range(1,m+1):
            insertion=D[i,j-1]
            deletion=D[i-1,j]
            match=D[i-1,j-1]+1
            mismatch=D[i-1,j-1]
            if a[i-1]==b[j-1]:
                D[i,j]=max(insertion,deletion,match)
            else:
                D[i,j]=max(insertion,deletion,mismatch)
    return D[m,n]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))

    n = data[0]
    data = data[1:]
    a = data[:n]

    data = data[n:]
    m = data[0]
    data = data[1:]
    b = data[:m]

    print(lcs2(a, b))
