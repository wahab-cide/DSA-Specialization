#2Sum Problem

def two_sum(nums, target):


    complements = dict()


    for i, num in enumerate(nums):
        complement = target - num

        if complement in complements:
            return [complements[complement], i]
        
        complements[num] = i

    return []




#3Sum Problem

    

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        nums.sort()
        triples = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            left, right = i + 1, len(nums) - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]

                if total < 0:
                    left += 1

                elif total > 0:
                    right -= 1
                else:
                    triples.append([nums[i], nums[left], nums[right]])
                    left += 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
        
        return triples
    
"""
 Given an integer array nums of length n and an integer target, find three integers in nums such that the sum is closest to target.

Return the sum of the three integers.

You may assume that each input would have exactly one solution.
"""

def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        closest_sum = float('inf')

        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]

                if abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum

                if current_sum < target:
                    left += 1

                elif current_sum > target:
                    right -= 1

                else:
                    return current_sum

        return closest_sum
