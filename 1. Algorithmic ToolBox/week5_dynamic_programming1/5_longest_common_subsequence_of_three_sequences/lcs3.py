#Uses python3

import sys
import numpy
def lcs3(a, b, c):
    #write your code here
    m=len(a)
    n=len(b)
    l=len(c)
    D=numpy.zeros((m+1,n+1,l+1),dtype=int)
    for k in range(1,l+1):
        for j in range(1,n+1):
            for i in range(1,m+1):
                insertion=D[i,j-1,k]
                deletion=D[i-1,j,k]
                match_=D[i,j,k-1]
                mismatch=D[i-1,j-1,k-1]
                insertion_=D[i,j-1,k-1]
                deletion_=D[i-1,j,k-1]
                match=D[i-1,j-1,k-1]+1
                mismatch_=D[i-1,j-1,k]
                if a[i-1]==b[j-1]==c[k-1]:
                    D[i,j,k]=max(insertion,deletion,insertion_,deletion_,match,match_,mismatch_)
                else:
                    D[i,j,k]=max(insertion,deletion,insertion_,deletion_,mismatch,match_,mismatch_)
    return D[m,n,l]

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    an = data[0]
    data = data[1:]
    a = data[:an]
    data = data[an:]
    bn = data[0]
    data = data[1:]
    b = data[:bn]
    data = data[bn:]
    cn = data[0]
    data = data[1:]
    c = data[:cn]
    print(lcs3(a, b, c))
