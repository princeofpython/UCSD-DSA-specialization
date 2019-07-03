# Uses python3
import sys
import numpy
def optimal_sequence(n):
    MinOps=numpy.zeros((n+1),dtype=int)
    for each in range(2,n+1):
        listt=[]
        if each%3==0:
            listt.append(MinOps[each//3]+1)
        if each%2==0:
            listt.append(MinOps[each//2]+1)
        listt.append(MinOps[each-1]+1)
        MinOps[each]=min(listt)
    return MinOps
def OutputAlignment(n,MinOps):
    if n==1:
        print(1,end=' ')
        return
    if n%3==0 and MinOps[n]==MinOps[n//3]+1:
        OutputAlignment(n//3,MinOps)
        print(n,end=' ')
    elif n%2==0 and MinOps[n]==MinOps[n//2]+1:
        OutputAlignment(n//2,MinOps)
        print(n,end=' ')
    else:
        OutputAlignment(n-1,MinOps)
        print(n,end=' ')
input = sys.stdin.read()
n = int(input)
MinOps=optimal_sequence(n)
print(MinOps[n])
OutputAlignment(n,MinOps)
