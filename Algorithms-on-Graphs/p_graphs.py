"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. 
You may assume all four edges of the grid are all surrounded by water.

 """
def numIslands(grid):
    if not grid:
        return 0
    
    rows, cols = len(grid), len(grid[0])
    islands = 0
    
    def dfs(r, c):
        # Check boundaries and water/visited cells
        if (r < 0 or c < 0 or 
            r >= rows or c >= cols or 
            grid[r][c] == '0'):
            return
        
        # Mark as visited by changing to '0'
        grid[r][c] = '0'
        
        # Check all 4 directions
        dfs(r+1, c)  # down
        dfs(r-1, c)  # up
        dfs(r, c+1)  # right
        dfs(r, c-1)  # left
    
    # Traverse the grid
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == '1':
                islands += 1
                dfs(r, c)
    
    return islands

"""
You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

Connect: A cell is connected to adjacent cells horizontally or vertically.
Region: To form a region connect every 'O' cell.
Surround: The region is surrounded with 'X' cells if you can connect the region with 'X' cells and 
none of the region cells are on the edge of the board.
A surrounded region is captured by replacing all 'O's with 'X's in the input matrix board."""

def solve(board):
    if not board or not board[0]:
        return
    
    m, n = len(board), len(board[0])
    
    def dfs(r, c):
        # Check boundaries and if cell is not 'O'
        if (r < 0 or c < 0 or 
            r >= m or c >= n or 
            board[r][c] != 'O'):
            return
        
        # Mark as safe by changing to a temporary character
        board[r][c] = 'S'  # S for Safe
        
        # Check all 4 directions
        dfs(r+1, c)  # down
        dfs(r-1, c)  # up
        dfs(r, c+1)  # right
        dfs(r, c-1)  # left
    
    # Step 1: Mark safe 'O's from borders
    
    # Check first and last row
    for c in range(n):
        dfs(0, c)
        dfs(m-1, c)
    
    # Check first and last column
    for r in range(m):
        dfs(r, 0)
        dfs(r, n-1)
    
    # Step 2: Capture surrounded regions
    for r in range(m):
        for c in range(n):
            if board[r][c] == 'O':    # Surrounded 'O'
                board[r][c] = 'X'
            elif board[r][c] == 'S':   # Safe 'O'
                board[r][c] = 'O'
def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """

        if not board or not board[0]:
            return

        m, n = len(board), len(board[0])


        def dfs(r, c):
            if r < 0 or c < 0 or r >= m or c >= n or board[r][c] != 'O':
                return
            board[r][c] == 'S'

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        #check 1st and last rows
        for r in range(n):
            dfs(0, r)  
            dfs(m - 1, r)

        #check first and last colums
        for c in range(m):
            dfs(c, 0)
            dfs(c, n - 1)     

        for r in range(m):
            for c in range(n):
                if board[r][c] == 'S':
                    board[r][c] = 'O'
                elif board[r][c] == 'O':
                    board[r][c] = 'X'  

"""
Given a reference of a node in a connected undirected graph.

Return a deep copy (clone) of the graph.

Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

class Node {
    public int val;
    public List<Node> neighbors;
}"""

#dfs
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def cloneGraph(node):
    if not node:
        return None
    
    # Hash map to store cloned nodes: original node -> cloned node
    cloned = {}
    
    def dfs(node):
        # If node is already cloned, return its clone
        if node in cloned:
            return cloned[node]
        
        # Create clone for current node
        clone = Node(node.val)
        # Add to hash map before DFS to handle cycles
        cloned[node] = clone
        
        # Clone all neighbors
        for neighbor in node.neighbors:
            clone.neighbors.append(dfs(neighbor))
            
        return clone
    
    return dfs(node)

'''
You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

Note: The variables that do not occur in the list of equations are undefined, so the answer cannot be determined for them.
'''
from collections import defaultdict

def calcEquation(equations, values, queries):
    # Build graph
    graph = defaultdict(dict)
    for (a, b), value in zip(equations, values):
        graph[a][b] = value
        graph[b][a] = 1.0 / value
    
    def dfs(start, end, visited):
        # If either variable is not in graph
        if start not in graph or end not in graph:
            return -1.0
            
        # If we found the target
        if start == end:
            return 1.0
            
        # Mark as visited
        visited.add(start)
        
        # Check all neighbors
        for neighbor, value in graph[start].items():
            if neighbor not in visited:
                result = dfs(neighbor, end, visited)
                if result != -1.0:
                    return value * result
        
        return -1.0
    
    # Process each query
    answers = []
    for numerator, denominator in queries:
        answers.append(dfs(numerator, denominator, set()))
    
    return answers


'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first 
if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.
'''