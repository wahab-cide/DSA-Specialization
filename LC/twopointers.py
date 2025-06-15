"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.


"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCnter(s, i, i + 1)

            maxLen = max(len1, len2)

            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i = (maxLen) // 2

        return s[start:end + 1]
    

    def expandAroundCenter(s, left, right):
        while left >= 0 and right < len(s) and s [left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


'''
CONTAINER WITH MOST WATER

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

from typing import List 
class Solution:
    def containerWithMostWater(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxWater = 0

        while left < right:
            currentWater = min(height[left], height[right]) * (right - left)
            maxWater = max(maxWater, currentWater)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater