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


def fourSum(self, nums, target):
        nums.sort()  # Sort the array first
        n = len(nums)
        result = []
        
        # Iterate over the first two numbers
        for i in range(n - 3):
            # Early exit if the smallest sum exceeds the target
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                break
            
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            
            # Early exit if the largest possible sum is less than the target
            if nums[i] + nums[n-1] + nums[n-2] + nums[n-3] < target:
                continue
            
            for j in range(i + 1, n - 2):
                # Skip duplicates for the second number
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                
                # Early exit for the second number
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    break

                if nums[i] + nums[j] + nums[n-1] + nums[n-2] < target:
                    continue
                
                # Now use two pointers for the remaining two numbers
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    
                    if total == target:
                        result.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        
                        # Skip duplicates for the third number
                        while left < right and nums[left] == nums[left - 1]:
                            left += 1
                        
                        # Skip duplicates for the fourth number
                        while left < right and nums[right] == nums[right + 1]:
                            right -= 1
                            
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
                        
        return result


"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""

def removeDuplicates(nums):
    if not nums:
        return 0  # Return 0 if nums is empty
    
    # Initialize the first pointer
    i = 0  # This points to the position of the last unique element
    
    # Traverse the array starting from the second element
    for j in range(1, len(nums)):
        # If the current element is different from the last unique element
        if nums[j] != nums[i]:
            i += 1  # Move the unique pointer
            nums[i] = nums[j]  # Update the position with the new unique element
    
    # The number of unique elements is i + 1
    return i + 1




"""
A permutation of an array of integers is an arrangement of its members into a sequence or linear order.

For example, for arr = [1,2,3], the following are all the permutations of arr: [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].
The next permutation of an array of integers is the next lexicographically greater permutation of its integer.
More formally, if all the permutations of the array are sorted in one container according to their lexicographical order, then the next permutation of that array is the permutation that follows it in the sorted container. If such arrangement is not possible, the array must be rearranged as the lowest possible order (i.e., sorted in ascending order).

For example, the next permutation of arr = [1,2,3] is [1,3,2].
Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not have a lexicographical larger rearrangement.
Given an array of integers nums, find the next permutation of nums."""


def nextPermutation(nums):
    # Step 1: Find the first decreasing element from the right
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1

    # Step 2: If such element was found, find the next larger element to swap with
    if i >= 0:
        j = len(nums) - 1
        while nums[j] <= nums[i]:
            j -= 1
        # Swap nums[i] and nums[j]
        nums[i], nums[j] = nums[j], nums[i]
    
    # Step 3: Reverse the elements to the right of the pivot to get the smallest permutation
    nums[i + 1:] = reversed(nums[i + 1:])
