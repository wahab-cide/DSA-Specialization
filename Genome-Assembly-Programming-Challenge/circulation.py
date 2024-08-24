from collections import defaultdict, deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.capacity = {}

    def add_edge(self, u,v,l,c):
        self.graph[u].append(v)
        self.graph[v].append(u)
        self.capacity[(u, v)] = c - l
        self.capacity[(v, u)] = 0

    def bfs(self, source, sink, parent):
        visited = [False] * self.V
        queue = deque([source])
        visited[source] = True

        while queue:
            u = queue.popleft()
            for v in self.graph[u]:
                if not visited[v] and self.capacity[(u, v)] > 0:
                    queue.append(v)
                    visited[v] = True
                    parent[v] = u
                    if v == sink:
                        return True
        return False
    
    def ford_fulkerson(self, source, sink):
        parent = [-1] * self.V
        max_flow = 0
        
        while self.bfs(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            
            while s != source:
                path_flow = min(path_flow, self.capacity[(parent[s], s)])
                s = parent[s]
            
            max_flow += path_flow
            v = sink
            
            while v != source:
                u = parent[v]
                self.capacity[(u, v)] -= path_flow
                self.capacity[(v, u)] += path_flow
                v = parent[v]
        
        return max_flow
    
def hasCirculation(V, edges, total_demand):
    g = Graph(V + 2)
    source = V
    sink = V + 1

    for u, v, l, c in edges:
        g.add_edge(u, v,l, c)

    max_flow = g.ford_fulkerson(source, sink)
    return max_flow == total_demand # outputs True if circulation exists