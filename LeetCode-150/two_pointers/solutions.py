"""
Given an array of positive integers nums and a positive integer target, 
return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

"""
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = 0
        curr = 0
        min_len = math.inf


        for right in range(len(nums)):
            curr += nums[right]

            while curr >= target:
                min_len = min(min_len, right - left + 1)
                curr -= nums[left]
                left += 1

        return min_len if min_len != math.inf else 0


# Given a string s, find the length of the longest substring without duplicate characters.
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_len = 0
        char_set = set()
        l = 0

        for r in range(len(s)):
            while s[r] in char_set:
                char_set.remove(s[l])
                l += 1
            char_set.add(s[r])
            max_len = max(max_len, r - l + 1)

        return max_len



"""
You are given a string s and an array of strings words. All the strings of words are of the same length.

A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.

For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. 
"acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.

"""

from collections import Counter

def findSubstring(s, words):
    if not s or not words:
        return []
    
    word_len = len(words[0])
    total_words = len(words)
    total_len = word_len * total_words
    result = []
    
    word_count = Counter(words)
    
    for i in range(word_len):
        left = i
        current_count = Counter()
        count = 0
        
        for j in range(i, len(s) - word_len + 1, word_len):
            word = s[j:j + word_len]
            
            if word in word_count:
                current_count[word] += 1
                count += 1
                
                while current_count[word] > word_count[word]:
                    left_word = s[left:left + word_len]
                    current_count[left_word] -= 1
                    count -= 1
                    left += word_len
                
                if count == total_words:
                    result.append(left)
            else:
                current_count.clear()
                count = 0
                left = j + word_len
    
    return result