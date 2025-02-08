#1 Unique Paths

def uniquePaths(m, n):
    dp = [[1] * n for _ in range(m)]

    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

    return dp[m - 1][n - 1]


#2 Longest common subsequence

def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i - 1] == text2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[m][n]

#3 Best Time to Buy and Sell Stock with Cooldown
def maxProfit(self, prices):
    if not prices:
        return 0
    n = len(prices)
    hold = [0] * n
    sold = [0] * n
    rest = [0] * n

    hold[0] = -prices[0]
    sold[0] = 0
    rest[0] = 0

    for i in range(1, n):
        hold[i] = max(hold[i - 1], rest[i - 1] - prices[i])
        sold[i] = hold[i - 1] + prices[i]
        rest[i] = max(rest[i - 1], sold[i - 1])

    return max(sold[-1], rest[-1])

#4 Coin Change II

def change(self, amount, coins):
    dp = [0] * (amount + 1)

    dp[0] = 1

    for coin in coins:
        for i in range(coin, amount + 1):
            dp[i] += dp[i - coin]
    return dp[amount]

#5 Target Sum
def findTargetSumWays(self, nums, target):
    total = sum(nums)

    if (total + target) % 2 != 0 or (total + target) < 0:
        return 0
    P = (total + target) / 2

    dp = [0] * (P + 1)

    for num in nums:
        for i in range(P, num - 1, -1):
            dp[i] += dp[i - num]

    return dp[P]

#6 Interleaving String

def isInterLeave(self, s1, s2, s3):
    m, n, k = len(s1), len(s2), len(s3)

    if (m + n) != k:
        return False
    dp = [[False] * (n + 1) * (m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        dp[i][0] = dp[i - 1][0] and s1[i - 1] == s3[i - 1]
    for j in range(1, n + 1):
        dp[0][j] = dp[0][ j - 1] and s2[j - 1] == s3[j - 1]
    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = (dp[i - 1][j] and s1[i - 1] == s3[ i + j - 1]) or (dp[i][j - 1] and s2[j - 1] == s3[i + j -1])

    return dp[m][n]


#7 Longest Increasing Path in Matrix
def longestIncreasingPath(self, matrix):
    if not matrix: return 0

    m, n = len(matrix), len(matrix[0])

    dp = [[0] * n for _ in range(m)]

    directions = [[1, 0], [-1, 0] [0, 1], [0, -1]]

    max_l = 1
    def dfs(i, j):
        if dp[i][j]:
            return dp[i][j]
        for dx, dy in directions:
            x, y = dx + i, dy + j
            if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
                max_l = max(max_l, 1 + dfs(x, y))
        dp[i][j] = max_l
        return dp[i][j]
    res = 0    
    for i in range(m):
        for j in range(n):
            res = max(res, dfs(i, j))
    return res

#8 Distinct Subsequences
def numDistinct(self, s, t):
    m, n = len(s), len(t)

    if n > m:
        return 0
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = 1
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[m][n]
            

#9 Edit Distance
def minDistance(self, word1, word2):
    m, n = len(word1), len(word2)

    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i
    for j in range(n + 1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j -1])

    return dp[m][n] 
from typing import List
#10 Burst Balloons
def maxCoins(nums: List[int]) -> int:
    n = len(nums)
    # Add 1 to the beginning and end of nums
    nums = [1] + nums + [1]
    # Initialize a DP table of size (n+2) x (n+2)
    dp = [[0] * (n + 2) for _ in range(n + 2)]
    
    # Fill the DP table
    for length in range(1, n + 1):  # Length of the subarray
        for i in range(1, n - length + 2):  # Start index of the subarray
            j = i + length - 1  # End index of the subarray
            for k in range(i, j + 1):  # Choose the last balloon to burst
                # Compute the coins for bursting the k-th balloon last
                coins = nums[i - 1] * nums[k] * nums[j + 1] + dp[i][k - 1] + dp[k + 1][j]
                # Update dp[i][j] with the maximum coins
                dp[i][j] = max(dp[i][j], coins)
    
    # The result is the value at dp[1][n]
    return dp[1][n]

#11 Regular Expression Matching
def isMatch(s: str, p: str) -> bool:
    m, n = len(s), len(p)
    # Initialize a DP table of size (m+1) x (n+1)
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    # Base case: empty string matches empty pattern
    dp[0][0] = True
    
    # Handle patterns like a*, a*b*, etc., that can match an empty string
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2]
    
    # Fill the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # Case 1: Ignore the '*' and the preceding character
                # Case 2: Use the '*' to match one or more occurrences of the preceding character
                dp[i][j] = dp[i][j - 2] or (dp[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
            else:
                # Current characters must match, and the previous characters must also match
                dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '.')
    
    # The result is the value at dp[m][n]
    return dp[m][n]

