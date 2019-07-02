# Uses python3
import sys

def get_majority_element(a, left, right):
    if left == right:
        return -1
    if left + 1 == right:
        return a[left]
    #write your code here
    mid=left+(right-left)//2
    A=get_majority_element(a, left, mid)
    B=get_majority_element(a, mid, right)

    if A==B:
        return A
    else:
        A_count=0
        B_count=0
        for i in range(left,right):
            if a[i]==B:
                B_count+=1
            if a[i]==A:
                A_count+=1
        if A_count>(right-left)/2:
            return A
        if B_count>(right-left)/2:
            return B
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
