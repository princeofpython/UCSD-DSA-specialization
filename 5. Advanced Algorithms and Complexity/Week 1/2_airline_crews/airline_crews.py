# python3
class MaxMatching:
    def read_data(self):
        n, m = map(int, input().split())
        adj_matrix = [list(map(int, input().split())) for i in range(n)]
        
        vertex_count = n + m + 2
        graph = FlowGraph(vertex_count, n)
        for i in range(n):
            graph.add_edge(0, i+1 , 1)
            for j in range(m):
                if adj_matrix[i][j] == 1:
                    graph.add_edge(i+1 , n+j+1, 1)
        for j in range(m):
            graph.add_edge(n+j+1, n+m+1, 1)
        return graph

    def write_response(self, matching):
        line = [str(-1 if x == -1 else x + 1) for x in matching]
        print(' '.join(line))

    '''
    def find_matching(self, adj_matrix):
        # Replace this code with an algorithm that finds the maximum
        # matching correctly in all cases.
        n = len(adj_matrix)
        m = len(adj_matrix[0])
        matching = [-1] * n
        busy_right = [False] * m
        for i in range(n):
            for j in range(m):
                if adj_matrix[i][j] and matching[i] == -1 and (not busy_right[j]):
                    matching[i] = j
                    busy_right[j] = True
        return matching
    '''

    def solve(self):
        graph = self.read_data()
        matching = max_flow(graph, 0, graph.size() - 1)
        self.write_response(matching)

import queue

class Edge:

    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# This class implements a bit unusual scheme for storing edges of the graph,
# in order to retrieve the backward edge for a given edge quickly.
class FlowGraph:

    def __init__(self, n, a):
        # List of all - forward and backward - edges
        self.edges = []
        # These adjacency lists store only indices of edges in the edges list
        self.graph = [[] for _ in range(n)]
        self.left = a

    def add_edge(self, from_, to, capacity):
        # Note that we first append a forward edge and then a backward edge,
        # so all forward edges are stored at even indices (starting from 0),
        # whereas backward edges are stored at odd indices.
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)
    
    def leftsize(self):
        return self.left

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        # To get a backward edge for a true forward edge (i.e id is even), we should get id + 1
        # due to the described above scheme. On the other hand, when we have to get a "backward"
        # edge for a backward edge (i.e. get a forward edge for backward - id is odd), id - 1
        # should be taken.
        #
        # It turns out that id ^ 1 works for both cases. Think this through!
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow
        self.edges[id].capacity -= flow
        self.edges[id ^ 1].capacity += flow
    
    def bfs(self, from_, to):
        q = queue.Queue()
        visited = [False]* self.size()
        
        q.put(from_)        
        visited[from_]=True
        prev=[(None, None)]*self.size()
        path=[]
        cap = float('inf')
        bPath = False
        
        while not q.empty():
            curr = q.get()
            for id in self.get_ids(curr):
                each = self.get_edge(id)
                if (not visited[each.v]) and each.capacity > 0:
                    q.put(each.v)
                    prev[each.v]=(curr,id)
                    visited[each.v]=True
                    
                    if to == each.v:
                        while(True):
                            path.append(id)
                            cap = min(cap, self.get_edge(id).capacity)
                            if curr == from_:
                                break
                            curr, id = prev[curr]
                        bPath = True
                        return bPath, path, cap
        return bPath, path, cap
    
def max_flow(graph, from_, to):
    flow = 0
    # your code goes here
    while(True):
        bPath, path, cap = graph.bfs(from_, to)
        if not bPath:
            break
        for id in path:
            graph.add_flow(id, cap)
        flow+=cap
    
    n = graph.leftsize()
    matching = [-1]*n
    for i in range(n):
        ids = graph.get_ids(i+1)
        for id in ids:
            edge = graph.get_edge(id)
            if edge.flow == 1 and edge.v!=0:
                matching[i]= edge.v - n -1
                break
    return matching
    

if __name__ == '__main__':
    max_matching = MaxMatching()
    max_matching.solve()
