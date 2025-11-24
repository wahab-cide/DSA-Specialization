"""
LeetCode 2204. Distance to a Cycle in Undirected Graph
You are given a positive integer n representing the number of nodes in a connected undirected graph containing exactly one cycle. The nodes are numbered from 0 to n - 1 (inclusive).

You are also given a 2D integer array edges, where edges[i] = [node1i, node2i] denotes that there is a bidirectional edge connecting node1i and node2i in the graph.

The distance between two nodes a and b is defined to be the minimum number of edges that are needed to go from a to b.

Return an integer array answer of size n, where answer[i] is the minimum distance between the ith node and any node in the cycle.

"""


from collections import defaultdict, deque
from typing import List

class Solution:
    def distanceToCycle(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for node1, node2 in edges:
            graph[node1].append(node2)
            graph[node2].append(node1)
        
        # Find one cycle using DFS
        visited = [False] * n
        parent = [-1] * n
        cycle_nodes = set()
        
        def find_cycle(node, par):
            visited[node] = True
            for nei in graph[node]:
                if nei == par:
                    continue
                if visited[nei]:
                    # Found a cycle
                    cur = node
                    while cur != nei:
                        cycle_nodes.add(cur)
                        cur = parent[cur]
                    cycle_nodes.add(nei)
                    return True
                else:
                    parent[nei] = node
                    if find_cycle(nei, node):
                        return True
            return False
        
        find_cycle(0, -1)
        
        # BFS from all cycle nodes
        distances = [-1] * n
        queue = deque()
        
        for node in cycle_nodes:
            distances[node] = 0
            queue.append(node)
        
        while queue:
            current = queue.popleft()
            for nei in graph[current]:
                if distances[nei] == -1:
                    distances[nei] = distances[current] + 1
                    queue.append(nei)
        
        return distances

    
"""
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.

"""
class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        if not nums: return 0

        max_num = max(nums)
        points = [0] * (max_num + 1)

        for num in nums:
            points[num] += num

        take, skip = 0, 0

        for i in range(max_num + 1):
            new_take = skip + points[i]
            new_skip = max(take, skip)
            take, skip = new_take, new_skip

        return max(take, skip)        