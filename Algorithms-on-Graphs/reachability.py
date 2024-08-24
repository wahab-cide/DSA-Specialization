import sys
from collections import deque

def reach(adj, x, y):
    # BFS implementation
    if x == y:
        return 1
    
    visited = [False] * len(adj)
    queue = deque([x])
    visited[x] = True
    
    while queue:
        node = queue.popleft()
        
        for neighbor in adj[node]:
            if not visited[neighbor]:
                if neighbor == y:
                    return 1
                visited[neighbor] = True
                queue.append(neighbor)
    
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
