# python3


def build_heap(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps

def leftChild(i):
    return 2*i+1

def rightChild(i):
    return 2*i+2

def parent(i):
    return (i-1)//2

def SiftDown(i,size,data):
    maxIndex=i
    l=leftChild(i)
    if l<size and data[l]<data[maxIndex]:
        maxIndex=l
    r=rightChild(i)
    if r<size and data[r]<data[maxIndex]:
        maxIndex=r
    if i!=maxIndex:
        data[i],data[maxIndex]=data[maxIndex],data[i]
        swaps.append((i,maxIndex))
        SiftDown(maxIndex,size,data)

def build_heap_fast(data,n):
    for i in range(n//2,-1,-1):
        SiftDown(i,n,data)

def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    global swaps
    swaps=[]
    build_heap_fast(data,n)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
'''
    swaps = build_heap_fast(data)
'''
if __name__ == "__main__":
    main()
