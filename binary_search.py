'''
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

1, 2, 8, 6, 5, 4, 3, 2, 0
'''

#we can treat the 2D matrix as a sorted 1D array and perform a binary search.
#Key insights:

#The entire matrix is effectively sorted when viewed as a 1D array
#We can convert 1D index to 2D matrix indices using division and modulo
#We can use binary search to achieve O(log(m * n)) time complexity

def searchMatrix(matrix: List[List[int]], target: int) -> bool:
    if not matrix or not matrix[0]:
        return False
    
    m, n = len(matrix), len(matrix[0])
    left, right = 0, m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        # Convert 1D index to 2D coordinates
        row = mid // n
        col = mid % n
        
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            left = mid + 1
        else:
            right = mid - 1
            
    return False





'''There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) 
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.'''

#The key insight is that in a rotated sorted array, 
# at any point, at least one half (left or right) must be sorted.


from collections import List

def search(nums: List[int], target: int) -> int:
    if not nums:
        return -1
    
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check if left half is sorted
        if nums[left] <= nums[mid]:
            # Check if target is in the left sorted half
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Right half must be sorted
        else:
            # Check if target is in the right sorted half
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
                
    return -1



'''Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.'''

#The key insight is that we need to find both the leftmost and rightmost positions of the target, so we'll perform two binary searches:

#One to find the leftmost position
#One to find the rightmost position

def searchRange(nums: List[int], target: int) -> List[int]:
    def findLeft(nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # If found target, try to find more on left
            if nums[mid] == target:
                if mid == 0 or nums[mid - 1] < target:
                    return mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    def findRight(nums, target):
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # If found target, try to find more on right
            if nums[mid] == target:
                if mid == len(nums) - 1 or nums[mid + 1] > target:
                    return mid
                left = mid + 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    
    if not nums:
        return [-1, -1]
        
    left = findLeft(nums, target)
    if left == -1:
        return [-1, -1]
    
    right = findRight(nums, target)
    return [left, right]



'''
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

[4,5,6,7,0,1,2] if it was rotated 4 times.
[0,1,2,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums of unique elements, return the minimum element of this array.

You must write an algorithm that runs in O(log n) time.


'''

# The key insight is that the minimum element is the pivot point where the rotation occurred, 
# and this pivot point is the only place where nums[i] > nums[i+1].
def findMin(nums: List[int]) -> int:
    if not nums:
        return 0
    
    left, right = 0, len(nums) - 1
    
    # If array is not rotated or rotated n times
    if nums[left] <= nums[right]:
        return nums[left]
    
    while left <= right:
        mid = (left + right) // 2
        
        # Found pivot point (minimum element)
        if mid < len(nums) - 1 and nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        if mid > 0 and nums[mid - 1] > nums[mid]:
            return nums[mid]
        
        # Decide which half to search
        if nums[mid] > nums[0]:
            # Minimum must be in right half
            left = mid + 1
        else:
            # Minimum must be in left half
            right = mid - 1
    
    return nums[0]  # Safeguard, should not reach here


    '''
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

'''
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        imin, imax, half_len = 0, m, (m + n + 1) // 2

        while imin <= imax:
            i = (imin + imax) // 2
            j = half_len - i
            
            if i < m and nums1[i] < nums2[j - 1]:
               
                imin = i + 1
            elif i > 0 and nums1[i - 1] > nums2[j]:
                
                imax = i - 1
            else:
               
                if i == 0: max_of_left = nums2[j - 1]
                elif j == 0: max_of_left = nums1[i - 1]
                else: max_of_left = max(nums1[i - 1], nums2[j - 1])

                
                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m: min_of_right = nums2[j]
                elif j == n: min_of_right = nums1[i]
                else: min_of_right = min(nums1[i], nums2[j])

                return (max_of_left + min_of_right) / 2.0


'''
A peak element is an element that is strictly greater than its neighbors.

Given a 0-indexed integer array nums, find a peak element, and return its index. If the array contains multiple peaks, return the index to any of the peaks.

You may imagine that nums[-1] = nums[n] = -∞. In other words, an element is always considered to be strictly greater than a neighbor that is outside the array.

You must write an algorithm that runs in O(log n) time.
'''




def searchRange(nums, target):
    def bin_search(nums, target, is_searching_left):
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left