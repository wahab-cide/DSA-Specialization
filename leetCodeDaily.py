from collections import defaultdict
"""
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) 
such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

"""

class Solution:
    from collections import defaultdict

    def tupleSameProduct(self, nums):
        n = len(nums)
        product_map = defaultdict(list)
        
       
        for i in range(n):
            for j in range(n):
                if i != j:
                    product = nums[i] * nums[j]
                    product_map[product].append((i, j))
        
        total = 0
        
        
        for product, pairs in product_map.items():
            
            unique_pairs = set()
            for i, j in pairs:
                a, b = nums[i], nums[j]
                if a < b:
                    unique_pairs.add((a, b))
                else:
                    unique_pairs.add((b, a))
            unique_pairs = list(unique_pairs)
            m = len(unique_pairs)
            
          
            count = 0
            for s_idx in range(m):
                s = unique_pairs[s_idx]
                s_elements = set(s)
                for t_idx in range(m):
                    if s_idx != t_idx:
                        t = unique_pairs[t_idx]
                        t_elements = set(t)
                        if s_elements.isdisjoint(t_elements):
                            count += 1
            
            total += count * 4
        
        return total

"""
You are given an integer limit and a 2D array queries of size n x 2.

There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. 
For every query in queries that is of the form [x, y], you mark ball x with the color y. 
After each query, you need to find the number of distinct colors among the balls.

Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.

Note that when answering a query, lack of a color will not be considered as a color.
"""

def queryResults(limit, queries):
    ball_color = dict()
    color_count = defaultdict(list)
    res = []

    for x, y in queries:
        old_color = ball_color.get(x)
        if old_color is not None:
            color_count[old_color] -= 1
            if color_count[old_color] == 0:
                del color_count[old_color]
        ball_color[x] = y
        color_count[y] += 1

        res.append(len(color_count))
    return res


"""
Design a number container system that can do the following:

Insert or Replace a number at the given index in the system.
Return the smallest index for the given number in the system.
Implement the NumberContainers class:

NumberContainers() Initializes the number container system.
void change(int index, int number) Fills the container at index with the number. 
If there is already a number at that index, replace it.
int find(int number) Returns the smallest index for the given number, 
or -1 if there is no index that is filled by number in the system.

"""
            
import bisect
from collections import defaultdict

class NumberContainers:
    def __init__(self):
        self.index_to_num = {} 
        self.num_to_indices = defaultdict(list)  

    def change(self, index: int, number: int) -> None:
        
        if index in self.index_to_num:
            old_num = self.index_to_num[index]
            
            idx = bisect.bisect_left(self.num_to_indices[old_num], index)
            if idx < len(self.num_to_indices[old_num]) and self.num_to_indices[old_num][idx] == index:
                self.num_to_indices[old_num].pop(idx)
        
       
        self.index_to_num[index] = number
       
        bisect.insort(self.num_to_indices[number], index)

    def find(self, number: int) -> int:
        
        if number in self.num_to_indices and self.num_to_indices[number]:
            return self.num_to_indices[number][0]
        return -1
    
"""
You are given a 0-indexed integer array nums. 
A pair of indices (i, j) is a bad pair if i < j and j - i != nums[j] - nums[i].

Return the total number of bad pairs in nums.
"""
from collections import Counter

def countBadPairs(self, nums):
    n = len(nums)
    if n < 2:
        return 0
    diff = [nums[i] - i for i in range(n)]

    freq = Counter(diff)

    good_pairs = sum(f * (f - 1) // 2 for f in freq.values())

    total_pairs = n * (n - 1) // 2
    bad_pairs = total_pairs - good_pairs

    return bad_pairs


"""
Given two strings s and part, perform the following operation on 
s until all occurrences of the substring part are removed:

Find the leftmost occurrence of the substring part and remove it from s.
Return s after removing all occurrences of part.

A substring is a contiguous sequence of characters in a string.

"""

def removeOccurrences(self, s, part):
    m = len(part)
    stack = []

    for char in s:
        stack.append(char)
        if len(stack) >= m and ''.join(stack[-m:]) == part:
            for _ in range(m):
                stack.pop()
    return ''.join(stack)


"""
You are given a 0-indexed array nums consisting of positive integers. 
You can choose two indices i and j, such that i != j, and 
the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain 
over all possible indices i and j that satisfy the conditions.
"""

def maximumSum(nums):
    def digitsSum(n):
        return sum(int(digit) for digit in str(n))
    
    map = defaultdict(list)

    for num in nums:
        s = digitsSum(num)
        map[s].append(num)
    maxSum = -1
    for s in map:
        if len(map[s]) >= 2:
            sortedNums = sorted(map[s], reverse=True)
            currSum = sortedNums[0] + sortedNums[1]
            maxSum = max(maxSum, currSum)

    return maxSum