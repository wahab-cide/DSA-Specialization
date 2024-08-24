from collections import defaultdict, deque

def build_de_bruijn_graph(reads, k):
    graph = defaultdict(list)
    in_degree = defaultdict(int)
    out_degree = defaultdict(int)
    
    for read in reads:
        for i in range(len(read) - k + 1):
            prefix = read[i:i + k - 1]
            suffix = read[i + 1:i + k]
            graph[prefix].append(suffix)
            out_degree[prefix] += 1
            in_degree[suffix] += 1
    
    return graph, in_degree, out_degree

def hasEulerianCycle(graph, in_degree, out_degree):
    for node in graph:
        if in_degree[node] != out_degree[node]:
            return False
    
    # Check if the graph is strongly connected
    start_node = next(iter(graph))
    visited = set()
    queue = deque([start_node])
    
    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
    
    return len(visited) == len(graph)

def find_optimal_k(reads):
    min_k = 1
    max_k = len(reads[0])
    
    for k in range(min_k, max_k + 1):
        graph, in_degree, out_degree = build_de_bruijn_graph(reads, k)
        
        if hasEulerianCycle(graph, in_degree, out_degree):
            return k
    
    return -1  # If no such k is found


