"""
two steps 
1. model the problem as a decision tree
2. implement dfs through the decison tree. 

nb: if you can clearly visualize the decision tree, 
you can easily solve it. 

"""
# Problem 1

# Given an array of unique characters, return all possible subsets in any order

def allSubsets(arr):
    res = []
    subset = []

    def visit(i):
        if i == len(arr):
            res.append(subset.copy())
            return

        subset.append(arr[i])
        visit(i + 1)
        subset.pop()
        visit(i + 1)

    visit(0)
    return res

# Problem 2

# Find all ways to place n non-attacking queens on an n * n board

def solveNQueens(n):
    res = []
    board = [['.'] * n for _ in range(n)]


    col = set()
    posDiag = set()
    negDiag = set()

    def visit(r):
        if r == n:
            copy = [''.join(row) for row in board]
            res.append(copy)
            return 
        
        for c in range(n):
            if (c in col or (r + c) in posDiag or (r - c) in negDiag):
                continue
            board[r][c] = 'Q'
            col.add(c)
            posDiag.add((r + c))
            negDiag.add((r - c))

            visit(r + 1)

            board[r][c] = '.'
            col.remove(c)
            posDiag.remove((r + c))
            negDiag.remove((r - c))
    visit(0)
    return res

# Problem 3

# Given a  non-empty array of unique characters, arr, return all possible permutations of arr, in any order

def permute(arr):

    if len(arr) == 1:
        return [arr[:]]
    
    res = []
    def visit(currPerm, remArr):
        if not remArr:
            res.append(currPerm[:])
        
        for i in range(len(remArr)):
            currChar = remArr[i]
            newRemArr = remArr[:i] + remArr[i + 1:]

            currPerm.append(currChar)
            visit(currPerm, newRemArr)

            currPerm.pop()

    visit([], arr)
    return res

# Problem 4

# Given an array of distinct integers, nums and a target integer, target, return a list of all unique combinations of nums 
# where the chosen numbers sum to target.

def combinationSum(nums, target):
    res = []
    def visit(start, currComb, remNum):
        if remNum == 0:
            res.append(currComb.copy())
            return
        if remNum < 0:
            return
        
        for i in range(start, len(nums)):
            currComb.append(nums[i])

            visit(i, currComb, remNum - nums[i])
            currComb.pop()
    visit(0, [], target)
    return res

#Problem 5

# Combination sum II

def CombinationSum2(candidates, target):

    res = []
    candidates.sort()
    def visit(start, currComb, remNum):
        if remNum == 0:
            res.append(currComb.copy())
            return
        if remNum < 0:
            return
        
        for i in range(start, len(candidates)):
            if i > start and candidates[i] == candidates[i - 1]:
                continue
            currComb.append(candidates[i])
            visit(i + 1, currComb, remNum - candidates[i])
            currComb.pop()

    visit(0, [], target)
    return res


#Problem 6

#Subsets II
from typing import List
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        subset = []
        nums.sort()
        def visit(start, subset):  
            res.append(subset.copy())
    
            for i in range(start, len(nums)):
                if i > start and nums[i] == nums[i - 1]:
                    continue
                subset.append(nums[i])
                visit(i + 1, subset)
                subset.pop()
        visit(0, [])
        return res
    
#Problem 7

#Problem 8

def partition(s):
    res = []

    def isPalindrome(substr):
        return substr == substr[::-1]

    def visit(start, currPartition):
        if start == len(s):
            res.append(currPartition.copy())
        for end in range(start, len(s)):
            substr = s[start:end + 1]

            if isPalindrome(substr):
                currPartition.append(substr)
                visit(end + 1, currPartition)
                currPartition.pop()
    visit(0, [])
    return res

def letterCombinations(digits):
    if not digits:
        return []
    phone_map = {
        '2': 'abc', 
        '3': 'def', 
        '4': 'ghi', 
        '5': 'jkl', 
        '6': 'mno', 
        '7': 'pqrs', 
        '8': 'tuv', 
        '9': 'wxyz'
        }
    res = []
    def visit(index, currCombination):
        if index == len(digits):
            res.append("".join(currCombination))
            return

        currDigit = digits[index]
        possibleLetters = phone_map[currDigit]

        for letter in possibleLetters:
            currCombination.append(letter)
            visit(index + 1, currCombination)
            currCombination.pop()
    visit(0, [])
    return res
