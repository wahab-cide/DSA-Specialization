"""
Longest Palindromic Substring

Given a string s, return the longest palindromic substring in s.


"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        start = 0
        end = 0

        for i in range(len(s)):
            len1 = self.expandAroundCenter(s, i, i)
            len2 = self.expandAroundCnter(s, i, i + 1)

            maxLen = max(len1, len2)

            if maxLen > end - start:
                start = i - (maxLen - 1) // 2
                end = i = (maxLen) // 2

        return s[start:end + 1]
    

    def expandAroundCenter(s, left, right):
        while left >= 0 and right < len(s) and s [left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1


'''
CONTAINER WITH MOST WATER

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.
'''

from typing import List, Optional 
class Solution:
    def containerWithMostWater(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1

        maxWater = 0

        while left < right:
            currentWater = min(height[left], height[right]) * (right - left)
            maxWater = max(maxWater, currentWater)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return maxWater
    


'''
3SUM
Given an integer array nums, return all the triplets 
[nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
'''

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        n = len(nums)
        res = []
        

        for i in range(n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total < 0:
                    left += 1
                elif total > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while right > left and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res


'''
fourSum
Given an array nums of n integers, return an array of all the unique quadruplets 
[nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
You may return the answer in any order.
'''

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []

        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left = j + 1
                right = n - 1

                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]

                    if total < target:
                        left += 1
                    elif total > target:
                        right -= 1
                    else:
                        res.append([nums[i], nums[j], nums[left], nums[right]])
                        while left < right and nums[left] == nums[left + 1]:
                            left += 1
                        while right > left and nums[right] == nums[right - 1]:
                            right -= 1
                        left += 1
                        right -= 1
        return res
    

'''
Remove Nth Node From End of List
Given the head of a linked list, remove the nth node from the end of the list and return its head.
'''
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        slow = fast = dummy

        for _ in range(n):
            fast = fast.next

        while fast.next:
            slow = slow.next
            fast = fast.next

        slow.next = slow.next.next
        return dummy.next



'''
Delete the Middle Node of a Linked List

You are given the head of a linked list. Delete the middle node, and return the head of the modified linked list.

The middle node of a linked list of size n is the ⌊n / 2⌋th node from the start using 0-based indexing, where ⌊x⌋ denotes the largest integer less than or equal to x.

For n = 1, 2, 3, 4, and 5, the middle nodes are 0, 1, 1, 2, and 2, respectively.


'''
class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next


class Solution:
    def deleteMiddle(head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        prev = None
        slow = fast = head

        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = slow.next

        return head
                