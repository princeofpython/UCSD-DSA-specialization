# Uses python3
import sys

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return [a[left]],number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)[1]
    number_of_inversions += get_number_of_inversions(a, b, ave, right)[1]
    #write your code here
    A=get_number_of_inversions(a, b, left, ave)[0]
    B=get_number_of_inversions(a, b, ave, right)[0]
    list_return=[]
    alen=(ave-left)
    blen=(right-ave)
    andex=0
    bndex=0
    while(andex<alen and bndex<blen):
        if A[andex]<=B[bndex]:
            list_return.append(A[andex])
            andex+=1
            number_of_inversions+=bndex
        else:
            list_return.append(B[bndex])
            bndex+=1
            #number_of_inversions+=bndex
    if bndex==blen:
        number_of_inversions+=(alen-andex)*bndex
    while(andex<alen):
        list_return.append(A[andex])
        andex+=1
    while(bndex<blen):
        list_return.append(B[bndex])
        bndex+=1
    #list_return=list_return+A+B
    return list_return,number_of_inversions

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a))[1])
