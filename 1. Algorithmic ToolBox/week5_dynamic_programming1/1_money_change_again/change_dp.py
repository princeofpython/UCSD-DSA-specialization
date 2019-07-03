# Uses python3
import sys
import numpy
def get_change(m):
    #write your code here
    MinNumCoins=numpy.zeros((m+1),dtype=int)
    for money in range(1,m+1):
        listt=[]
        for coin in [1,3,4]:
            if money>=coin:
                listt.append(MinNumCoins[money-coin]+1)
        MinNumCoins[money]=min(listt)
    return MinNumCoins[m]



if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(get_change(m))
