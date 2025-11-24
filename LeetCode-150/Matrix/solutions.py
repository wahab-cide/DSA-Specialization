"""
Given an m x n binary grid grid where each 1 marks the home of one friend, return the minimal total travel distance.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|
"""
from typing import List


class Solution:
    def minTotalDistance(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])


        rows = []
        cols = []

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    rows.append(i)

        print(rows)

        for j in range(n):
            for i in range(m):
                if grid[i][j] == 1:
                    cols.append(j)

        median_r = rows[len(rows) // 2]
        median_cols = cols[len(cols) // 2]

        total = 0

        for r in rows:
            total += abs(r - median_r)
        for c in cols:
            total += abs(c - median_cols)

        return total


"""
You are given an m x n grid grid of values 0, 1, or 2, where:

each 0 marks an empty land that you can pass by freely,
each 1 marks a building that you cannot pass through, and
each 2 marks an obstacle that you cannot pass through.
You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.
"""
from collections import deque
import math

class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])

        total_distance = [[0] * n for _ in range(m)]
        reach_count = [[0] * n for _ in range(m)]


        def bfs(i, j):
            visited = [[False] * n for _ in range(m)]
            visited[i][j] = True

            queue = deque([(i, j, 0)])

            while queue:
                row, col, dist = queue.popleft()

                for dr, dc in [[1, 0], [-1, 0], [0, -1], [0, 1]]:
                    r, c = row + dr, col + dc
                    if(0 <= r < m and 0 <= c < n and not visited[r][c] and grid[r][c] == 0):

                        visited[r][c] = True
                        new_dist = dist + 1


                        reach_count[r][c] += 1
                        total_distance[r][c] += new_dist
                        queue.append((r, c, new_dist))


        total_buildings = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    bfs(i, j)
                    total_buildings += 1

        min_distance = math.inf
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 and reach_count[i][j] == total_buildings:
                    min_distance = min(min_distance, total_distance[i][j])

        return min_distance if min_distance != math.inf else -1

    
"""
Given an m x n matrix grid where each cell is either a wall 'W', an enemy 'E' or empty '0', return the maximum enemies you can kill using one bomb. You can only place the bomb in an empty cell.

The bomb kills all the enemies in the same row and column from the planted point until it hits the wall since it is too strong to be destroyed.
"""
class Solution:
    def maxKilledEnemies(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
    
        m, n = len(grid), len(grid[0])
        max_kills = 0
        
        row_hits = 0
        col_hits = [0] * n  # col_hits[j] = enemies killed in column j from current segment
        
        for i in range(m):
            for j in range(n):
                # Recalculate row_hits at start of row or after a wall
                if j == 0 or grid[i][j - 1] == 'W':
                    row_hits = 0
                    # Count enemies in this row segment (until wall or end)
                    k = j
                    while k < n and grid[i][k] != 'W':
                        if grid[i][k] == 'E':
                            row_hits += 1
                        k += 1
                
                # Recalculate col_hits[j] at start of column or after a wall
                if i == 0 or grid[i - 1][j] == 'W':
                    col_hits[j] = 0
                    # Count enemies in this column segment (until wall or end)
                    k = i
                    while k < m and grid[k][j] != 'W':
                        if grid[k][j] == 'E':
                            col_hits[j] += 1
                        k += 1
                
                # If current cell is empty, we can place a bomb here
                if grid[i][j] == '0':
                    max_kills = max(max_kills, row_hits + col_hits[j])
        
        return max_kills




        