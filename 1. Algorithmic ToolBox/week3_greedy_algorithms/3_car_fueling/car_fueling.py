# python3
import sys


def compute_min_refills(distance, tank, stops):
    # write your code here
    stops.append(distance)
    last_refill=0
    dist=0
    num=0
    i=-1
    while(dist<distance):
        while(dist<distance and last_refill+tank>=stops[i+1] ):
            i+=1
            dist=stops[i]
        if dist==last_refill:
            return -1
        num+=1
        last_refill=dist
    num-=1
    return num

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    #d,m,n=[int(i) for i in input().split()]
    #stops=[int(i) for i in input().split()]
    print(compute_min_refills(d, m, stops))
