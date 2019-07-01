# Uses python3
import sys

def get_change(m):
    #write your code here
    count=0
    while(m>0):
        if m>=10:
            m=m-10
        elif m>=5:
            m-=5
        elif m>=1:
            m-=1
        count+=1
    return count

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
