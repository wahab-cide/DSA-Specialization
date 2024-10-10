#Interference-free Robot Scheduling



from collections import deque

# Function to calculate shortest path distance between two nodes using BFS
def graph_distance(G, u, v):
    # BFS to compute shortest path distance between u and v
    if u == v:
        return 0
    queue = deque([u])
    distances = {u: 0}
    
    while queue:
        current = queue.popleft()
        current_distance = distances[current]
        
        for neighbor in G[current]:
            if neighbor not in distances:
                distances[neighbor] = current_distance + 1
                if neighbor == v:
                    return distances[neighbor]
                queue.append(neighbor)
    
    # If there is no path from u to v, return a large number
    return float('inf')

# Function to check if an interference-free schedule exists
def is_interference_free_schedule(G, a, b, c, d, r):
    # BFS initialization
    queue = deque([(a, b)])  # Start from (a, b)
    visited = set([(a, b)])  # Track visited states

    while queue:
        x, y = queue.popleft()  # Current positions of robots 1 and 2
        
        # Check if we've reached the goal state
        if x == c and y == d:
            return True  # Found an interference-free schedule
        
        # Generate all possible next moves for both robots
        for next_x in G[x]:  # Neighbors of robot 1's current position
            for next_y in G[y]:  # Neighbors of robot 2's current position
                if (next_x, next_y) not in visited:
                    # Check the distance between next_x and next_y
                    if graph_distance(G, next_x, next_y) >= r:
                        # Valid state, add to queue
                        queue.append((next_x, next_y))
                        visited.add((next_x, next_y))

    return False  # No interference-free schedule found

# Example Usage
if __name__ == '__main__':
    # Graph representation as adjacency list
    G = {
        1: [2, 3],
        2: [1, 4],
        3: [1, 4],
        4: [2, 3, 5],
        5: [4]
    }

    a = 1  # Starting position of robot 1
    b = 5  # Starting position of robot 2
    c = 4  # Goal position of robot 1
    d = 2  # Goal position of robot 2
    r = 2  # Minimum required distance between the robots

    result = is_interference_free_schedule(G, a, b, c, d, r)
    if result:
        print("There is an interference-free schedule.")
    else:
        print("There is no interference-free schedule.")



