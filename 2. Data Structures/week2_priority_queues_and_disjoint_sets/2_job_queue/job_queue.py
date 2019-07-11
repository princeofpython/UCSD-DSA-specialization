# python3

from collections import namedtuple

AssignedJob = namedtuple("AssignedJob", ["started_at", "worker" ])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result

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
        SiftDown(maxIndex,size,data)

def build_heap_fast(data,n):
    for i in range(n//2,-1,-1):
        SiftDown(i,n,data)

def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    data=[]

    for _ in range(n_workers):
        data.append([0,_])

    for each in jobs:
        print(data[0][1],data[0][0])
        data[0][0]+=each
        SiftDown(0,n_workers,data)
'''
    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)
'''

if __name__ == "__main__":
    main()
