#Sliding Window

"""

Problem 1:
Given an array of integers, 
find the maximum sum of contiguous 
subarray of size k.

"""

def max_subarray_sum(arr, k):
    window_sum = sum(arr[:k])
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum

# Example usage
arr = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(max_subarray_sum(arr, k))  # Output: 16


#Problem 2
def length_of_longest_substring(s): 
    char_map = {} # stores most recent index where each character occured
    left = 0
    max_length = 0

    for right in range(len(s)):
        if s[right] in char_map and char_map[s[right]] >= left:
            left = char_map[s[right]] + 1
        char_map[s[right]] = right
        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
s = "abcabcbb"
print(length_of_longest_substring(s))  # Output: 3

#Problem 3
def max_consecutive_ones(nums):
    max_length = 0
    left = 0
    zero_count = 0

    for right in range(len(nums)):
        if nums[right] == 0:
            zero_count += 1

        while zero_count > 1:
            if nums[left] == 0:
                zero_count -= 1
            left += 1

        max_length = max(max_length, right - left + 1)

    return max_length

# Example usage
nums = [1, 0, 1, 1, 0]
print(max_consecutive_ones(nums))  # Output: 4


#Binary search

#Problem 1
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Example usage
arr = [1, 3, 5, 7, 9, 11, 13]
target = 7
print(binary_search(arr, target))  # Output: 3


"""
Problem 2:

Given a sorted array of integers, 
find the first occurrence of a target value.

"""
def first_occurrence(arr, target):
    left, right = 0, len(arr) - 1
    result = -1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching to the left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result

# Example usage
arr = [1, 2, 2, 3, 4, 4, 4, 5]
target = 4
print(first_occurrence(arr, target))  # Output: 4

"""
Problem 3:

Given a sorted array of integers, 
find the peak element. A peak element 
is an element that is greater than its neighbors.

"""
def find_peak_element(arr):
    left, right = 0, len(arr) - 1
    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] > arr[mid + 1]:
            right = mid
        else:
            left = mid + 1
    return left

# Example usage
arr = [1, 2, 3, 1]
print(find_peak_element(arr))  # Output: 2

#Two Heaps or Priority Queues

"""
Problem 1:

Implement a data structure that supports 
adding elements and finding the median of 
the elements in constant time.

"""
import heapq

class MedianFinder:
    def __init__(self):
        self.min_heap = []
        self.max_heap = []

    def add_num(self, num):
        if not self.max_heap or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        if len(self.max_heap) > len(self.min_heap) + 1:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def find_median(self):
        if len(self.max_heap) == len(self.min_heap):
            return (-self.max_heap[0] + self.min_heap[0]) / 2
        else:
            return -self.max_heap[0]

# Example usage
mf = MedianFinder()
mf.add_num(1)
mf.add_num(2)
print(mf.find_median())  # Output: 1.5

"""
Problem 2:

Given an array of integers and an integer k, 
find the median of each window of size k as 
it slides through the array.
"""

import heapq

def median_sliding_window(nums, k):
    min_heap = []
    max_heap = []
    result = []

    for i, num in enumerate(nums):
        if not max_heap or num <= -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        if i >= k:
            if nums[i - k] <= -max_heap[0]:
                max_heap.remove(-nums[i - k])
                heapq.heapify(max_heap)
            else:
                min_heap.remove(nums[i - k])
                heapq.heapify(min_heap)
        while len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        while len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        if i >= k - 1:
            if k % 2 == 0:
                result.append((-max_heap[0] + min_heap[0]) / 2)
            else:
                result.append(-max_heap[0])

    return result

# Example usage
nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
print(median_sliding_window(nums, k))  # Output: [1, -1, 3, 5, 5, 6]

"""
Problem 3:

Given a stream of integers, 
find the kth largest 
element at any given time.

"""
import heapq

def kth_largest_element(nums, k):
    min_heap = []

    for num in nums:
        if len(min_heap) < k:
            heapq.heappush(min_heap, num)
        elif num > min_heap[0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, num)

    return min_heap[0]

# Example usage
nums = [4, 5, 8, 2]
k = 3
print(kth_largest_element(nums, k))  # Output: 4

#Graph Traversal

"""
Problem 1:

Perform a breadth-first search (BFS) to 
find the shortest path between two nodes 
in an undirected graph.

"""

from collections import defaultdict, deque

def shortest_path(graph, start, end):
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        node, path = queue.popleft()
        if node == end:
            return path
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    return []

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0],
    3: [1, 5],
    4: [1],
    5: [3]
}
start = 0
end = 5
print(shortest_path(graph, start, end))  # Output: [0, 1, 3, 5]

"""
Problem 2:

Given an undirected graph, 
check if it is a tree (no cycles and connected).

"""
def is_tree(graph):
    visited = set()

    def dfs(node, parent):
        if node in visited:
            return False
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor != parent and not dfs(neighbor, node):
                return False
        return True

    # Check for cycle
    if not dfs(0, -1):
        return False
    # Check if all nodes are visited
    return len(visited) == len(graph)

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1, 4],
    4: [3]
}
print(is_tree(graph))  # Output: True

"""
Problem 3:

Find the number of connected components 
in an undirected graph.

"""
def num_connected_components(graph):
    visited = set()
    count = 0

    def dfs(node):
        visited.add(node)
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs(neighbor)

    for node in graph:
        if node not in visited:
            dfs(node)
            count += 1

    return count

# Example usage
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1, 4],
    4: [3]
}
print(num_connected_components(graph))  # Output: 1


#Dynamic Programming

"""
Problem 1:

Calculate the nth Fibonacci number using 
dynamic programming.

"""

def fibonacci(n):
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]

# Example usage
n = 6
print(fibonacci(n))  # Output: 8

"""
Problem 2:

Find the length of the longest increasing 
subsequence in an array.

"""
def length_of_lis(nums):
    if not nums:
        return 0
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))  # Output: 4

"""
Problem 3:

Given a string, find the length of the 
longest palindromic subsequence.

"""
def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]
    for i in range(n):
        dp[i][i] = 1
    for l in range(2, n + 1):
        for i in range(n - l + 1):
            j = i + l - 1
            if s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])
    return dp[0][n - 1]

# Example usage
s = "bbbab"
print(longest_palindromic_subsequence(s))  # Output: 4


#Recursion

#1 Calculate the nth Fibonacci number:

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
n = 6
print(fibonacci(n))  # Output: 8


#2 Find the length of the longest increasing subsequence:

def length_of_lis(nums):
    def lis_recursive(nums, prev, current):
        if current == len(nums):
            return 0
        taken = 0
        if nums[current] > prev:
            taken = 1 + lis_recursive(nums, nums[current], current + 1)
        not_taken = lis_recursive(nums, prev, current + 1)
        return max(taken, not_taken)

    return lis_recursive(nums, float('-inf'), 0)

# Example usage
nums = [10, 9, 2, 5, 3, 7, 101, 18]
print(length_of_lis(nums))  # Output: 4

#3 Find the length of the longest palindromic subsequence:

def longest_palindromic_subsequence(s):
    def lps_recursive(s, start, end):
        if start > end:
            return 0
        if start == end:
            return 1
        if s[start] == s[end]:
            return 2 + lps_recursive(s, start + 1, end - 1)
        else:
            return max(lps_recursive(s, start + 1, end), lps_recursive(s, start, end - 1))

    return lps_recursive(s, 0, len(s) - 1)

# Example usage
s = "bbbab"
print(longest_palindromic_subsequence(s))  # Output: 4