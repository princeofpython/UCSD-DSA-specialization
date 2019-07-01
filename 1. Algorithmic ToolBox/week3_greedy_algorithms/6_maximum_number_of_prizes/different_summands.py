# Uses python3
import sys

def optimal_summands(n):
    summands = []
    #write your code here
    var=1
    while(True):
        if (n>=2*var+1):
            summands.append(var)
        else:
            summands.append(n)
            break
        n-=var
        var+=1
    return summands

if __name__ == '__main__':
    #input = sys.stdin.read()
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    for x in summands:
        print(x, end=' ')
