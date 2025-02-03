#1 Number of islands
from collections import deque
from typing import List, Optional

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0

        def bfs(r, c): 
            q = deque()
            visited.add((r, c))
            q.append((r, c))


            while q:
                row, col = q.popleft()
                dxs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for dr, dc in dxs:
                    r, c = row + dr, col + dc

                    if r in range(rows) and c in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
                        q.append((r, c))
                        visited.add((r, c))

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1' and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1

        return islands
    

#2 Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def dfs(r, c):
            
            if (r < 0 or c < 0 or r == rows or c == cols or grid[r][c] == 0 or (r, c) in visited):
                return 0
            visited.add((r, c))
            return 1 + (dfs(r + 1, c) +
                        dfs(r - 1, c) +
                        dfs(r, c + 1) +
                        dfs(r, c - 1)) 

        area = 0
        for r in range(rows):
            for c in range(cols):
                area = max(area, dfs(r, c))
        return area
    
#3 Clone Graph


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = dict()

        def clone(node):
            if node in oldToNew:
                return oldToNew[node] 
            copy = Node(node.val)
            oldToNew[node] = copy

            for nei in node.neighbors:
                copy.neighbors.append(clone(nei))
            return copy
        
        return clone(node) if node else None
        

#4 Islands and Treasure

"""
You are given a 
m × n
m×n 2D grid initialized with these three possible values:

-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.
Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest than the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.
"""

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows, cols = len(grid), len(grid[0])
        visited = set()
        q = deque()

        def addGrid(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or (r, c) in visited or grid[r][c] == -1):
                return
            visited.add((r, c))
            q.append([r, c])

      
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    q.append([r, c])
                    visited.add((r, c))

        dist = 0
        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                grid[r][c] = dist
                addGrid(r + 1, c)
                addGrid(r - 1, c)
                addGrid(r, c + 1)
                addGrid(r, c -1)
            dist += 1


#5 Rotting fruit
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        time, fresh = 0, 0
        q = deque()


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append([r, c])
                if grid[r][c] == 1:
                    fresh += 1
        dxs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in dxs:
                    row, col = dr + r, dc + c
                    if (row < 0 or col < 0 or row == rows or col == cols or grid[row][col] != 1):
                        continue
                  
                    grid[row][col] = 2
                    q.append([row, col])
                    fresh -= 1

            time += 1
        return time if fresh == 0 else -1



#6 Pacific Atlantic Water Flow
class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows, cols = len(heights), len(heights[0])
        pac, atl = set(), set()

        def dfs(r, c, visited, prevHeight):
            if ((r, c) in visited or r < 0 or c < 0 or r == rows or c == cols or heights[r][c] < prevHeight):
                return
            visited.add((r, c))
            dxs = [[1, 0], [-1, 0],[0, 1], [0, -1]]
            for dr, dc in dxs:
                row, col = r + dr, c + dc
                dfs(row, col, visited, heights[r][c])


        for r in range(rows):
            dfs(r, 0,pac, heights[r][0] )
            dfs(r, cols - 1, atl, heights[r][cols - 1])

        for c in range(cols):
            dfs(0, c, pac, heights[0][c])
            dfs(rows - 1, c, atl, heights[rows - 1][c])

        res = []
        for r in range(rows):
            for c in range(cols):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res



#7  Surrounded regions
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows, cols = len(board), len(board[0])

        def capture(r, c):
            if (r < 0 or c < 0 or r == rows or c == cols or board[r][c] != 'O'):
                return
            board[r][c] = 'S'

            dxs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in dxs:
                row, col = r + dr, c + dc
                capture(row, col)
        

        for r in range(rows):
            for c in range(cols):
                if (board[r][c] == 'O' and r in [0, rows - 1] or c in [0, cols - 1]):
                    capture(r, c)

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'O':
                    board[r][c] = 'X'

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == 'S':
                    board[r][c] = 'O'


        

        
#8 Course Schedule
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        visited = set()

        for crs, pre in prerequisites:
            preMap[crs].append(pre)

        def dfs(crs):
            if crs in visited: 
                return False
            if preMap[crs] == []:
                return True
            visited.add(crs)
            for pre in preMap[crs]:
                if not dfs(pre): return False
            visited.remove(crs)
            preMap[crs] = []
            return True

        for crs in range(numCourses):
            if not dfs(crs): return False
        return True


#9 Course Schedule II
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}

        for crs, pre in prerequisites:
            preMap[crs].append(pre)


        res = []
        visited, cycle = set(), set()


        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visited:
                return True
            cycle.add(crs)
            for pre in preMap[crs]:
                if dfs(pre) == False:
                    return False        
            cycle.remove(crs)
            visited.add(crs)
            res.append(crs)

        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return res
    
#10 Graph valid Tree

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        
        adj = { i:[] for i in range(n) }

        for n1, n2 in edges:
            adj[n1].append(n2)
            adj[n2].append(n1)

        visit = set()
        def dfs(n, prev):
            if n in visit:
                return False
            visit.add(n)

            for nei in adj[n]:
                if nei == prev:
                    continue
                if not dfs(nei, n):
                    return False
            return True
        
        return dfs(0, -1) and n == len(visit)
    

#11 num connected components Union Find
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        par = [i for i in range(n)]
        rank =[1] * n

        def find(n):
            res = n

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return 0
            
            if rank[p1] > rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]

            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return 1
        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res



#12 redundant connection
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            res = n

            while res != par[res]:
                par[res] = par[par[res]]
                res = par[res]
            return res
        
        def union(n1, n2):
            p1, p2 = find(n1), find(n2)

            if p1 == p2:
                return False
            
            if rank[p1] < rank[p2]:
                par[p1] = p2
                rank[p2] += rank[p1]

            else:
                par[p2] = p1
                rank[p1] += rank[p2]
            return True
        
        for n1, n2 in edges:
            if union(n1, n2) == False:
                return [n1, n2]

#13 Word ladder
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        pass

        
        