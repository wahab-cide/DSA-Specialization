"""
Given a string s, find the length of the longest 
substring without repeating characters.


Sliding window, Dictionary
"""

def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        char_index = dict()
        max_l = 0

        start = 0

        for end in range(len(s)):
            char = s[end]

            if char in char_index and char_index[char] >= start:
                start = char_index[char] + 1

            char_index[char] = end

            max_l = max(max_l, end - start + 1)

        return max_l


"""
Given a string s, return the longest 
palindromic substring in s.
"""

def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def expandAroundCenter(left, right):

            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1

            return s[left + 1:right]

        if len(s) <= 1:
            return s

        longest = ""


        for i in range(len(s)):

            odd_palindrome = expandAroundCenter(i, i)
            even_plaindrome = expandAroundCenter(i, i + 1)


            longest = max(longest,odd_palindrome,even_plaindrome, key=len)

        return longest