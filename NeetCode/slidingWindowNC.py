#  1 Buy, Sell stock

def buySell(prices):

    l, r = 0, 1
    maxP = 0

    while r < len(prices):

        if prices[l] < prices[r]:
            profit = prices[r] - prices[l]
            maxP = max(maxP, profit)

        else:
            l = r

        r += 1

    return maxP

# 2 longest substring with no rep characters

def lengthOfLongestSubstring(s):
    charSet = set()
    l = 0
    res = 0

    for r in range(len(s)):

        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1

        charSet.add(s[r])
        res = max(res, r - l + 1)

# 3 characterreplacement

def charReplacement(s, k):

    count = dict()
    l = 0
    res = 0

    for r in range(len(s)):
        count[s[r]] = 1 + count.get(s[r], 0)

        while (r - l + 1) - max(count.values()) > k:
            count[s[l]] -= 1
            l += 1


        res  = max(res, r - l + 1)

    return res

# 4 permutation in string 

'''
Permutation in String
You are given two strings s1 and s2.

Return true if s2 contains a permutation of s1, or false otherwise. 
That means if a permutation of s1 exists as a substring of s2, then return true.

Both strings only contain lowercase letters.

'''


# 5 minimum window substring

'''
Given two strings s and t, return the shortest substring of s such that every character in t, 
including duplicates, is present in the substring. If such a substring does not exist, return an empty string "".

You may assume that the correct output is always unique.
'''
