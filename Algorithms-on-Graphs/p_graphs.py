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

from collections import defaultdict, deque

def canFinishKahn(numCourses, prerequisites):
    # Build adjacency list and indegree count
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    
    # Start with courses that have no prerequisites
    queue = deque([course for course in range(numCourses) if indegree[course] == 0])
    
    courses_taken = 0
    
    while queue:
        current = queue.popleft()
        courses_taken += 1
        
        # Complete this course and update prerequisites
        for next_course in graph[current]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    return courses_taken == numCourses

'''
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. 
You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take 
course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, 
return any of them. If it is impossible to finish all courses, return an empty array.
'''

from collections import defaultdict, deque

def findOrder(numCourses, prerequisites):
    # Build adjacency list and indegree count
    graph = defaultdict(list)
    indegree = [0] * numCourses
    
    # Build graph
    for course, prereq in prerequisites:
        graph[prereq].append(course)
        indegree[course] += 1
    
    # Start with courses that have no prerequisites
    queue = deque([course for course in range(numCourses) 
                  if indegree[course] == 0])
    
    order = []  # Store the course order
    
    # Process all courses
    while queue:
        current = queue.popleft()
        order.append(current)  # Add current course to order
        
        # Process all courses that depend on current course
        for next_course in graph[current]:
            indegree[next_course] -= 1
            if indegree[next_course] == 0:
                queue.append(next_course)
    
    # Return order if all courses can be taken, empty list otherwise
    return order if len(order) == numCourses else []


# graph BFS
"""
You are given an n x n integer matrix board where the cells are labeled from 1 to n2 in a Boustrophedon style starting from the bottom left of the board (i.e. board[n - 1][0]) and alternating direction each row.

You start on square 1 of the board. In each move, starting from square curr, do the following:

Choose a destination square next with a label in the range [curr + 1, min(curr + 6, n2)].
This choice simulates the result of a standard 6-sided die roll: i.e., there are always at most 6 destinations, regardless of the size of the board.
If next has a snake or ladder, you must move to the destination of that snake or ladder. Otherwise, you move to next.
The game ends when you reach the square n2.
A board square on row r and column c has a snake or ladder if board[r][c] != -1. The destination of that snake or ladder is board[r][c]. Squares 1 and n2 are not the starting points of any snake or ladder.

Note that you only take a snake or ladder at most once per dice roll. If the destination to a snake or ladder is the start of another snake or ladder, you do not follow the subsequent snake or ladder.

For example, suppose the board is [[-1,4],[-1,3]], and on the first move, your destination square is 2. You follow the ladder to square 3, but do not follow the subsequent ladder to 4.
Return the least number of dice rolls required to reach the square n2. If it is not possible to reach the square, return -1

"""

class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        def get_pos(s):
            r, c = divmod(s - 1, n)
            if r % 2 == 1:
                c = n - c - 1
            r = n - r - 1
            return r, c

        queue = deque([(1, 0)])
        visited = {1}

        while queue:
            curr, moves = queue.popleft()
            if curr == n * n:
                return moves

            for i in range(1, 7):
                next_square = curr + i
                if next_square > n * n:
                    continue
                row, col = get_pos(next_square)
                if board[row][col] != -1:
                    next_square = board[row][col]
                
                if next_square not in visited:
                    visited.add(next_square)
                    queue.append((next_square, moves + 1))

        return -1


"""
A gene string can be represented by an 8-character long string, with choices from 'A', 'C', 'G', and 'T'.

Suppose we need to investigate a mutation from a gene string startGene to a gene string endGene where one mutation is defined as one single character changed in the gene string.

For example, "AACCGGTT" --> "AACCGGTA" is one mutation.
There is also a gene bank bank that records all the valid gene mutations. A gene must be in bank to make it a valid gene string.

Given the two gene strings startGene and endGene and the gene bank bank, return the minimum number of mutations needed to mutate from startGene to endGene. If there is no such a mutation, return -1.

Note that the starting point is assumed to be valid, so it might not be included in the bank.

"""

class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:

        if endGene not in bank:
            return -1

        bank = set(bank)   
        chars = ['A', 'C', 'G', 'T']
        queue = deque([(startGene, 0)])
        visited = {startGene}

        while queue:
            currGene, mutations = queue.popleft()
            if currGene == endGene:
                return mutations
            
            for i in range(8):
                for char in chars:
                    if char == currGene[i]:
                        continue

                    mutation = currGene[:i] + char + currGene[i + 1:]
                    if mutation in bank and mutation not in visited:
                        visited.add(mutation)
                        queue.append((mutation, mutations + 1))

        return -1



"""
A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

"""

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList: return 0

        word_len = len(beginWord)
        patterns = defaultdict(list)

        for word in wordList:
            for i in range(word_len):
                pattern = word[:i] + '*' + word[i + 1:]
                patterns[pattern].append(word)


        queue = deque([(beginWord, 1)])
        visited = {beginWord}

        while queue:
            currWord, lengthLadder = queue.popleft()

            if currWord == endWord:
                return lengthLadder

            for i in range(word_len):
                pattern = currWord[:i] + '*' + currWord[i + 1:]

                for word in patterns[pattern]:
                    if word not in visited:
                        visited.add(word)
                        queue.append((word, lengthLadder + 1))


        return 0
        