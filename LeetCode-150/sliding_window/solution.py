"""
Given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. 
If there is no such subarray, return 0 instead.
"""
import math
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        l = 0
        curr_sum = 0
        min_length = math.inf

        for i in range(len(nums)):
            curr_sum += nums[i]

            while curr_sum >= target:
                min_length = min(min_length, i - l + 1)
                curr_sum -= nums[l]
                l += 1

        return min_length if min_length != math.inf else 0
        









# More Problems
# Given a string s, return the length of the longest substring that contains at most two distinct characters.

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if not s:
            return 0
        char_count = dict()

        l = 0
        max_len = 0

        for r, char in enumerate(s):
            char_count[char] = char_count.get(char, 0) + 1
            while len(char_count) > 2:
                char_count[s[l]] -= 1
                if char_count[s[l]] == 0:
                    del char_count[s[l]]
                l += 1

            max_len = max(max_len, r - l + 1)


        return max_len


"""
187. Repeated DNA Sequences
Medium

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

"""
from typing import List
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        max_len = 10
        seen = set()
        repeated = set()

        #number of sequence of length 10 in a string of length n where n >= 10 = n - 9
        for i in range(len(s) - max_len + 1):
            curr = s[i:i + max_len]
            if curr in seen:
                repeated.add(curr)
            else:
                seen.add(curr)
        return list(repeated)
    
#219  Contains Duplicate I
#Given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k.
def containsDuplicateII(nums, k):
    indices = dict()

    for i, num in enumerate(nums):
        if num in indices and i - indices[num] <= k:
            return True
        indices[num] = i
    return False


#220. Contains Duplicate III
#You are given an integer array nums and two integers indexDiff and valueDiff. Find a pair of indices (i, j) such that:
from bisect import bisect_left, insort
class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        if indexDiff < 0:
            return False
        window = []


        for i, num in enumerate(nums):
            pos = bisect_left(window, num - valueDiff)

            if pos < len(window) and window[pos] <= num + valueDiff:
                return True
            insort(window, num)

            if i >= indexDiff:
                window.pop(bisect_left(window, nums[i - indexDiff]))

        return False

