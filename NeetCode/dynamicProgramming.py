"""
memo = {}  # Memoization map to store subproblem results

def f(subproblem_id):
    # Base case: handle the simplest subproblems
    if subproblem is base case:
        return result directly
    
    # Check if the subproblem is already solved
    if subproblem_id in memo:
        return memo[subproblem_id]
    
    # Recurrence relation: solve the subproblem and store the result
    memo[subproblem_id] = recurrence_relation_formula
    return memo[subproblem_id]

# Start solving the problem
return f(initial_subproblem_id)

"""



#1 Climbing stairs
def climbStairs(n):

    memo = dict()

    def f(x):
        if x <= 2:
            return x
        if x in memo:
            return memo[x]
        memo[x] = f(x - 1) + f(x - 2)
        return memo[x]
    return f(n)

#2 Min cost climbing stairs
def minCostClimbingStairs(cost):
    memo = dict()

    def dp(i):
        if i >= len(cost):
            return 0
        if i in memo:
            return memo[i]
        memo[i] = cost[i] + min(dp(i + 1), dp(i + 2))
        return memo[i]
    return min(dp(0), dp(1))

#3 House Robber
def rob(nums):
    memo = {}

    def visit(i):
        if i >= len(nums):
            return 0
        if i == len(nums) - 1:
            return nums[i]
        if i in memo:
            return memo[i]
        memo[i] = max(nums[i] + visit(i + 2), visit(i + 1))
        return memo[i]
    
    return max(nums[0] + visit(2), visit(1))

#4 House Robber II

def rob(nums):
    if len(nums) <= 3:
        return max(nums)
    
    def robRange(start, end):
        memo = dict()

        def dp(i):
            if i > end: return 0
            if i in memo: return memo[i]
            memo[i] = max(nums[i] + dp(i + 2), dp(i + 1))
            return memo[i]
        return dp(start)
    return max(robRange(0, len(nums) - 2), robRange(1, len(nums) - 1))

#5 Decode ways

def numDecodings(s):
    n = len(s)
    memo = {}

    def dp(i):
        if i == n:
            return 1
        if int(s[i]) == 0:
            return 0
        if i in memo:
            return memo[i]
        ways = dp(i + 1)
        if i + 1 < n and int(s[i:i + 2]) <= 26:
            ways += dp(i + 2)
        memo[i] = ways
        return ways
    return dp(0)

#6 Coin Change
def coinChange(coins, amount):
    if not coins: return -1

    memo = {}

    def dp(target):
        if target == 0: return 0
        if target < 0: return float('inf')
        if target in memo: return memo[target]

        result = [1 + dp(target - coin) for coin in coins if target >= coin]

        if result:
            memo[target] = min(result)
            return memo[target]
        return float('inf')
    
    res = dp(amount)
    return res if res != float('inf') else -1

#7 Maximum Product Subarray
def maxProduct(self, nums):
        if not nums: return 0

        maxSoFar = minSoFar = result = nums[0]

        for num in nums[1:]:
            candidates = (num, maxSoFar * num, minSoFar * num)
            maxSoFar = max(candidates)
            minSoFar = min(candidates)
            result = max(result, maxSoFar)

        return result

#8 Word Break

def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        wordSet = set(wordDict)
        memo = {}

        def dp(i):
            if i == n: return True
            if i in memo: return memo[i]
            
            for w in wordSet:
                if s[i:i+len(w)] == w: 
                    if dp(i + len(w)):
                        memo[i] = True
                        return True 
            memo[i] = False
            return False

        return dp(0)

#9 Longest Increasing Subsequence
def lengthOfLIS(nums):
    n = len(nums)
    if n == 0:
        return 0
    dp = [1] * n
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)
    return max(dp)

#10 Partition Equal Subset Sum
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False  
        target = totalSum // 2
        memo = {}

        def dp(i, currSum):
            if currSum == target:
                return True  
            if i >= len(nums) or currSum > target:
                return False  

            if (i, currSum) in memo:
                return memo[(i, currSum)]

           
            memo[(i, currSum)] = dp(i + 1, currSum + nums[i]) or dp(i + 1, currSum)
            return memo[(i, currSum)]

        return dp(0, 0)
