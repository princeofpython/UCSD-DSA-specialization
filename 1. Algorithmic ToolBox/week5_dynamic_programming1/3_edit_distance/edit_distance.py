# Uses python3
import numpy
def edit_distance(A, B):
    #write your code here
    m=len(A)
    n=len(B)
    D=numpy.zeros((m+1,n+1),dtype=int)
    for i in range(n+1):
        D[0,i]=i
    for i in range(m+1):
        D[i,0]=i
    for j in range(1,n+1):
        for i in range(1,m+1):
            insertion=D[i,j-1]+1
            deletion=D[i-1,j]+1
            match=D[i-1,j-1]
            mismatch=D[i-1,j-1]+1
            if A[i-1]==B[j-1]:
                D[i,j]=min(insertion,deletion,match)
            else:
                D[i,j]=min(insertion,deletion,mismatch)
    return D[m,n]

if __name__ == "__main__":
    print(edit_distance(input(), input()))
