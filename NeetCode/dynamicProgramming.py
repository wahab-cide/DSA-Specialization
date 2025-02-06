memo = {}  # Memoization map to store subproblem results
"""

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