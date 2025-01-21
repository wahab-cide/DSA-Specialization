def getMinTikTokServer(x, y):
    """
    Calculate the minimum cost to build a server network.

    Args:
        x: List[int] - x-coordinates of servers
        y: List[int] - y-coordinates of servers

    Returns:
        int - Minimum cost to connect all servers
    """
    class UnionFind:
        def __init__(self, size):
            self.parent = list(range(size))
            self.rank = [0] * size

        def find(self, node):
            if self.parent[node] != node:
                self.parent[node] = self.find(self.parent[node])  # Path compression
            return self.parent[node]

        def union(self, node1, node2):
            root1 = self.find(node1)
            root2 = self.find(node2)

            if root1 != root2:
                if self.rank[root1] > self.rank[root2]:
                    self.parent[root2] = root1
                elif self.rank[root1] < self.rank[root2]:
                    self.parent[root1] = root2
                else:
                    self.parent[root2] = root1
                    self.rank[root1] += 1
                return True
            return False

    n = len(x)
    # List to store all edges (cost, server1, server2)
    edges = []

    # Sorting by x-coordinates and forming edges
    sorted_by_x = sorted(range(n), key=lambda i: x[i])
    for i in range(n - 1):
        cost = abs(x[sorted_by_x[i + 1]] - x[sorted_by_x[i]])
        edges.append((cost, sorted_by_x[i], sorted_by_x[i + 1]))

    # Sorting by y-coordinates and forming edges
    sorted_by_y = sorted(range(n), key=lambda i: y[i])
    for i in range(n - 1):
        cost = abs(y[sorted_by_y[i + 1]] - y[sorted_by_y[i]])
        edges.append((cost, sorted_by_y[i], sorted_by_y[i + 1]))

    # Sort edges by cost
    edges.sort()

    # Apply Kruskal's algorithm
    uf = UnionFind(n)
    min_cost = 0
    edges_used = 0

    for cost, server1, server2 in edges:
        if uf.union(server1, server2):
            min_cost += cost
            edges_used += 1
            if edges_used == n - 1:  # All servers are connected
                break

    return min_cost