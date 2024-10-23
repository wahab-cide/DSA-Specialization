"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a 
subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

"""
def minSubArrayLen(target, nums):
    start = 0  # Starting pointer of the sliding window
    current_sum = 0  # Current sum of the sliding window
    min_length = float('inf')  # Initialize to infinity
    
    # Iterate through the array with the end pointer
    for end in range(len(nums)):
        current_sum += nums[end]  # Add the current element to the sum
        
        # Shrink the window while the current sum is greater than or equal to the target
        while current_sum >= target:
            min_length = min(min_length, end - start + 1)  # Update the minimal length
            current_sum -= nums[start]  # Shrink the window by moving the start pointer
            start += 1
    
    # If min_length was updated, return it; otherwise, return 0 (no valid subarray found)
    return min_length if min_length != float('inf') else 0


"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting 
some (can be none) of the characters without disturbing the relative positions of the remaining characters. 
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).

"""
def isSubsequence(s, t):
    i, j = 0, 0  # Pointers for s and t
    
    # Traverse t with j while matching characters from s with i
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1  # Move the pointer for s if there's a match
        j += 1  # Always move the pointer for t
    
    # If we've matched all characters of s, return True
    return i == len(s)



"""
Given an array of integers, find the maximum sum of contiguous subarray of size k.
"""


def max_sum_arr(arr, k):

    window_sum = sum(arr[:k])
    max_sum = window_sum


    for i in range(k, len(arr)):
        window_sum = window_sum - arr[i - k] + arr[i]
        max_sum = max(max_sum, window_sum)

    return max_sum


"""
Given a string, find the length of the longest substring without repeating characters.
"""

def longestSubstring(s):

    char_index = dict()
    start = 0
    max_len = 0


    for end in range(len(s)):
        if s[end] in char_index and char_index[s[end]] >= start:
            start = char_index[s[end]] + 1
        char_index[s[end]] = end
        max_len = max(max_len, end - start + 1)

    return max_len
        

