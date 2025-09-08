# 22 categories


#remove duplicates  I 26
from typing import List


def removeDuplicates(nums):
    # Edge case: If the array is empty, return 0
    if not nums:
        return 0

    # Initialize the pointer for the unique elements
    k = 1

    # Iterate through the array starting from the second element
    for i in range(1, len(nums)):
        # If the current element is different from the previous element
        if nums[i] != nums[i - 1]:
            # Place it at the next unique position
            nums[k] = nums[i]
            k += 1
    
    # Return the number of unique elements
    return k


#remove duplicates II 80
def removeDuplicates(nums):
    # Edge case: if the array is empty or has only one or two elements, return its length
    if len(nums) <= 2:
        return len(nums)
    
    # Initialize the pointer for the next position
    k = 2  # We can always keep the first two elements since we want each element to appear at most twice
    
    # Iterate through the array starting from the third element
    for i in range(2, len(nums)):
        # Compare the current element with the element two places before it
        if nums[i] != nums[k - 2]:
            # If it's not equal, it means it's allowed to be placed
            nums[k] = nums[i]
            k += 1
    
    # Return the number of elements in the modified array
    return k


#majority element
def majorityElement(nums):
    # Phase 1: Boyer-Moore Voting Algorithm to find the candidate
    count = 0
    candidate = None

    for num in nums:
        if count == 0:
            candidate = num
        if num == candidate:
            count += 1
        else:
            count -= 1
    
    # Return the candidate since it's guaranteed to be the majority element
    return candidate

#jump game
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        n = len(nums)

        for i in range(n):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= n - 1:
                return True
        return False

# Jump Game II
class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0
        
        jumps = 0
        curr_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])
            if i == curr_end:
                jumps += 1
                curr_end = farthest
                if curr_end >= n - 1:
                    break

        return jumps
    
    #gas station

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:

        total_gas = 0
        total_cost = 0
        current_tank = 0
        start_idx = 0

        for i in range(len(gas)):
            total_gas += gas[i]
            total_cost += cost[i]
            current_tank += gas[i] - cost[i]
            if current_tank < 0:
                start_idx = i + 1
                current_tank = 0

        return start_idx if total_gas >= total_cost else -1
        

#Candy
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
    
#Trapping Rain Water
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left , right = 0, len(height)
        left_max, right_max = height[left], height[right]
        trapped = 0

        while left < right:
            if left_max < right_max:
                left += 1
                left_max = max(left_max, height[left])
                trapped += left_max - height[left]

            else:
                right -= 1
                right_max = max(right_max, height[right])
                trapped += right_max - height[right]

        return trapped
    
#Roman to integer
class Solution:
    def romanToInt(self, s: str) -> int:
        romanMap = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
        }
        
        total = 0

        n = len(s)

        for i in range(n):
            if i < n - 1 and romanMap[s[i]] < romanMap[s[i + 1]]:
                total -= romanMap[s[i]]
            else:
                total += romanMap[s[i]]

        return total
    
    #Value to roman
class Solution:
    def intToRoman(self, num: int) -> str:
        val_to_roman = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I')
        ]

        ROMAN = []
        for value, symbol in val_to_roman:
            while value <= num:
                ROMAN.append(symbol)
                num -= value

        return ''.join(ROMAN)
    

#Length of last word
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s) - 1

        while i >= 0 and s[i] == ' ':
            i -= 1

        length = 0
        while i >= 0 and s[i] != ' ':
            length += 1
            i -= 1

        return length
    

#zigzag conversion
'''
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);
'''
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        
        rows = [""] * numRows
        current = 0
        going_down = False

        for char in s:
            rows[current] += char
            if current == 0 or current == numRows - 1:
                going_down = not going_down
            current += 1 if going_down else -1
        return "".join(rows)