#Uses python3
import sys
import math

def distance(xi, yi, xj, yj):
    return ((xi - xj)**2 + (yi - yj)**2)**0.5


def minimum_distance(vertices, adj, weight):
    result = 0.
    X = set()
    X.add(0)

    while len(X) != vertices:
        minimum=float('inf')
        for u in X:
            for v in adj[u]:
                if v not in X and weight[u][v] < minimum:
                    minimum = weight[u][v]
                    edge=v
        result += minimum
        X.add(edge)

    return result


if __name__ == '__main__':
    user_input = sys.stdin.read()
    data = list(map(int, user_input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    adj = [[] for _ in range(n)]
    weight = [[0] * n for _ in range(n)]
    for i in range(n):
        adj[i] = list(v for v in range(n) if v != i)
        for j in range(n):
            if i != j:
                w = distance(x[i], y[i], x[j], y[j])
                weight[i][j] = w
                weight[j][i] = w

    print("{0:.9f}".format(minimum_distance(n, adj, weight)))