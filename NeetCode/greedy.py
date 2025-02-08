#1 Maximum Subarray

def maxSubArray(self, nums):
    if not nums:  return 0

    currSum = maxSum = nums[0]

    for num in nums[1:]:
        currSum = max(num, currSum + num)
        maxSum = max(maxSum, currSum)

    return maxSum

#2 Jump Game
def canJump(self, nums):
    if not nums: return False
    if len(nums) == 1: return True

    farthest = 0
    for i in range(len(nums)):
        if i > farthest: return False
        farthest =  max(farthest, i + nums[i])
        if farthest >= len(nums) - 1: return True
    return False

#2 Jump Game II
def jump(self, nums):
        if not nums:
            return 0
        if len(nums) == 1:
            return 0
        
        jumps = 0
        current_end = 0
        farthest = 0
        
        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest
                if current_end >= len(nums) - 1:
                    break
        return jumps
            