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
