Sliding Window:

Sliding window problems involve maintaining 
a dynamic window over a sequential data structure 
(e.g., an array or string) and efficiently 
processing elements as the window “slides” 
from one position to another.

Problem 1:

Given an array of integers, 
find the maximum sum of contiguous subarray of size k.

Solution: Use a sliding window of size k to iterate 
through the array. At each step, add the current 
element to the window sum and subtract the element 
that falls out of the window. Keep track of the 
maximum sum encountered.


Problem 2:

Given a string, find the length of the longest 
substring without repeating characters.

Solution: Use a sliding window to maintain a 
substring without repeating characters. 
Start with an empty window and expand it by 
adding characters from the string. 
If a repeating character is found, 
shrink the window from the left until 
the repeating character is removed.


Problem 3:

Given a binary array, find the maximum number of consecutive 1s in this array if you can flip at most one 0.

Solution: Use a sliding window to iterate through the array. Maintain a count of zeros in the window. If the count of zeros exceeds one, shrink the window from the left until the count is valid. Update the maximum length of consecutive 1s seen so far.


Binary Search

Binary search is an algorithm used to find the position of a target value within a sorted array. It works by repeatedly dividing the search interval in half. Here’s how it works, followed by three common problems and solutions using binary search:

Problem 1:

Given a sorted array of integers, return the index of the target value. If the target is not found, return -1.

Solution: Use binary search to find the target value in the array.

Problem 2:

Given a sorted array of integers, find the first occurrence of a target value.

Solution: Use binary search, but instead of returning when the target is found, continue searching to the left to find the first occurrence.

Problem 3:

Given a sorted array of integers, find the peak element. A peak element is an element that is greater than its neighbors.

Solution: Use binary search to find the peak element. Compare the middle element with its neighbors to determine if it is a peak. If not, move towards the higher neighbor.




Two Heaps or Priority Queues

The Two Heaps pattern is used to efficiently maintain and retrieve elements while satisfying specific conditions.

A heap is a specialized tree-based data structure. It essentially combines the structure of a binary tree with a specific order based on the values stored in the nodes.

Here’s an explanation along with three common problems and solutions using this pattern:

Problem 1:

Implement a data structure that supports adding elements and finding the median of the elements in constant time.

Solution: Use two heaps, a max-heap to store the smaller half of the elements and a min-heap to store the larger half. The median will be the root of the max-heap or the average of the roots if the heaps are of different sizes.

Problem 2:

Given an array of integers and an integer k, find the median of each window of size k as it slides through the array.

Solution: Use two heaps to maintain the window. Remove elements that fall out of the window and add new elements as the window slides. Calculate the median using the heaps.

Problem 3:

Given a stream of integers, find the kth largest element at any given time.

Solution: Use a min-heap to store the k largest elements seen so far. If a new element is larger than the root of the min-heap, replace the root with the new element and heapify.


Graph Traversal

Graph traversal involves visiting all the nodes in a graph in a systematic way. Here’s an explanation of graph traversal, followed by three common problems and solutions using graph traversal techniques like breadth-first search (BFS) and depth-first search (DFS):

Problem 1:

Perform a breadth-first search (BFS) to find the shortest path between two nodes in an undirected graph.

Solution: Use BFS to traverse the graph starting from the source node. Keep track of the parent of each node to reconstruct the shortest path from the source to the destination.

Problem 2:

Given an undirected graph, check if it is a tree (no cycles and connected).

Solution: Use DFS or BFS to traverse the graph. If all nodes are visited and there are no back edges, the graph is a tree.


Problem 3:

Find the number of connected components in an undirected graph.

Solution: Use DFS or BFS to traverse the graph, keeping track of visited nodes. Each time you start a new traversal from an unvisited node, increment the count of connected components.


Dynamic Programming

Dynamic programming is a technique used to solve problems by breaking them down into smaller overlapping subproblems. Here’s an explanation of dynamic programming, followed by three common problems and solutions using dynamic programming:

Problem 1:

Calculate the nth Fibonacci number using dynamic programming.

Solution: Use a bottom-up approach to calculate Fibonacci numbers iteratively, storing previously calculated values to avoid redundant calculations.

Problem 2:

Find the length of the longest increasing subsequence in an array.

Solution: Use dynamic programming to keep track of the length of the longest increasing subsequence ending at each index of the array.

Problem 3:

Given a string, find the length of the longest palindromic subsequence.

Solution: Use dynamic programming to build a table where dp[i][j] stores the length of the longest palindromic subsequence in the substring from index i to j.


Recursion

Recursion is a programming technique where a function calls itself to solve smaller instances of the same problem. It’s based on the concept of dividing a problem into smaller, more manageable subproblems, and then combining the results of those subproblems to solve the original problem.

In dynamic programming, the top-down approach, also known as memoization, uses recursion to solve problems by breaking them down into smaller subproblems. It starts by solving the top-level problem and recursively solves the smaller subproblems, storing their results in a data structure (often a memoization table or array) to avoid redundant calculations. When a subproblem is encountered again, its solution is retrieved from the data structure rather than recalculating it. This approach helps improve efficiency by reducing the number of repeated calculations.

While recursion can be elegant and concise, it can also be less efficient in terms of memory usage and execution time compared to iterative solutions, especially for problems with deep recursion or overlapping subproblems. However, for many problems, the simplicity and readability of recursive solutions can outweigh these concerns.

Here is how the 3 dynamic programming problems above will be solved by recursion : top — down approach:

Calculate the nth Fibonacci number:





Summary
###### ####
Sliding Window: This technique involves maintaining a dynamic window over a sequential data structure and efficiently processing elements as the window “slides” from one position to another. We’ve covered examples such as finding the maximum sum of a contiguous subarray and the length of the longest substring without repeating characters.
Binary Search: Binary search is used to find the position of a target value within a sorted array. We’ve discussed examples like finding the index of a target value in a sorted array and finding the peak element in a sorted array.
Two Heaps (or Priority Queues): This pattern involves using two heaps, typically a max-heap and a min-heap, to efficiently maintain and retrieve elements while satisfying specific conditions. We’ve covered examples such as implementing a data structure that supports adding elements and finding the median of the elements in constant time.
Graph Traversal: Graph traversal involves navigating through graphs or trees. We’ve discussed examples such as performing a breadth-first search (BFS) to find the shortest path between two nodes in an undirected graph and finding the number of connected components in an undirected graph.
Dynamic Programming: Dynamic programming requires solving problems by breaking them down into smaller overlapping subproblems. We’ve discussed examples like calculating the nth Fibonacci number and finding the length of the longest increasing subsequence in an array.