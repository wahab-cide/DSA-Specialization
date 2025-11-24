"""
You are given an m x n grid rooms initialized with these three possible values.

-1 A wall or an obstacle.
0 A gate.
INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

"""
from collections import deque
from typing import List
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """

        m, n = len(rooms), len(rooms[0])
        INF = 2**31 - 1


        queue = deque()
        for i in range(m):
            for j in range(n):
                if rooms[i][j] == 0:
                    queue.append((i, j))

        while queue:
            row, col = queue.popleft()

            for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
                r, c = row + dr, col + dc

                if (0 <= r < m and 0 <= c < n and rooms[r][c] == INF):
                    rooms[r][c] = rooms[row][col] + 1
                    queue.append((r, c))



"""
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. 
You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

"""
        
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:


        m, n = len(matrix), len(matrix[0])
        dp = [[0] * n for _ in range(m)]


        def dfs(i, j):
            if dp[i][j] != 0:
                return dp[i][j]
            max_path = 1

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                r, c = i + dr, j + dc

                if (0 <= r < m and 0 <= c < n and matrix[r][c] > matrix[i][j]):
                    max_path = 1 + dfs(r, c)

            dp[i][j] = max_path
            return max_path


        

        res = 0
        for i in range(m):
            for j in range(n):
                res = max(res, dfs(i, j))

        return res


""""
You are asked to design a file system that allows you to create new paths and associate them with different values.

The format of a path is one or more concatenated strings of the form: / followed by one or more lowercase English letters. 
For example, "/leetcode" and "/leetcode/problems" are valid paths while an empty string "" and "/" are not.


Implement the FileSystem class:

bool createPath(string path, int value) Creates a new path and associates a value to it if possible and returns true. 
Returns false if the path already exists or its parent path doesn't exist.
int get(string path) Returns the value associated with path or returns -1 if the path doesn't exist.
"""

class FileSystem:

    def __init__(self):
        self.root = {"value": None}
        

    def createPath(self, path: str, value: int) -> bool:
        if not path or path[0] != "/" or path == '/':
            return False
        components = path.split("/")[1:]

        current = self.root
        for i in range(len(components) - 1):
            component = components[i]
            if component not in current:
                return False
            current = current[component]


        final_component = components[-1]
        if final_component in current:
            return False
        current[final_component] = {"value": value}
        return True

        

    def get(self, path: str) -> int:
        if not path or path == '/' or path[0] != "/": return -1

        components = path.split("/")[1:]

        current = self.root
        for component in components:
            if component not in current:
                return -1
            current = current[component]

        return current["value"]
        


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)



"""
You are given an n x n binary matrix grid. You are allowed to change at most one 0 to be 1.

Return the size of the largest island in grid after applying this operation.

An island is a 4-directionally connected group of 1s.

"""

#Key Insight:  The key insight is to use connected component labeling and then check each 0 to see which islands it could connect.

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def dfs(i, j, island_id):
            if ( not (0 <= i < n) or not (0 <= j < n) or grid[i][j] != 1):
                return 0

            grid[i][j] = island_id
            size = 1

            for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                size += dfs(i + dr, j + dc, island_id)

            return size


        #label all islands with unique id
        island_sizes = dict()
        island_id = 2

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    size = dfs(i, j, island_id)
                    island_sizes[island_id] = size
                    island_id += 1

        max_island = max(island_sizes.values()) if island_sizes else 0

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 0:
                    neighboring_islands = set()
                    for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                        dx, dy = i + dr, j + dc
                        if (0 <= dx < n and 0 <= dy < n and grid[dx][dy] > 1):
                            neighboring_islands.add(grid[dx][dy])

                    new_size = 1
                    for neighbor in neighboring_islands:
                        new_size += island_sizes[neighbor]

                    max_island = max(max_island, new_size)

        return max_island      




"""
You are given n tasks labeled from 0 to n - 1 represented by a 2D integer array tasks, where tasks[i] = [enqueueTimei, processingTimei] 
means that the i'th task will be available to process at enqueueTimei and will take processingTimei to finish processing.

You have a single-threaded CPU that can process at most one task at a time and will act in the following way:

If the CPU is idle and there are no available tasks to process, the CPU remains idle.
If the CPU is idle and there are available tasks, the CPU will choose the one with the shortest processing time. 
If multiple tasks have the same shortest processing time, it will choose the task with the smallest index.
Once a task is started, the CPU will process the entire task without stopping.
The CPU can finish a task then start a new one instantly.
Return the order in which the CPU will process the tasks."""

import heapq

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        n = len(tasks)
        
        # Add original indices to tasks
        indexed_tasks = [(enqueue, process, i) for i, (enqueue, process) in enumerate(tasks)]
        
        # Sort tasks by enqueue time
        indexed_tasks.sort()
        
        # Min heap for available tasks: (processing_time, original_index)
        min_heap = []
        
        result = []
        time = 0
        task_idx = 0
        
        while task_idx < n or min_heap:
            # If no tasks available, jump to next enqueue time
            if not min_heap and task_idx < n:
                time = max(time, indexed_tasks[task_idx][0])
            
            # Add all tasks that are available at current time
            while task_idx < n and indexed_tasks[task_idx][0] <= time:
                enqueue, process, idx = indexed_tasks[task_idx]
                heapq.heappush(min_heap, (process, idx))
                task_idx += 1
            
            # Process the next task
            if min_heap:
                process_time, original_idx = heapq.heappop(min_heap)
                result.append(original_idx)
                time += process_time
        
        return result



        