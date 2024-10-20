"""Given an integer array nums, move all 0's to the end of 
it while maintaining the relative order of the non-zero elements. 
Note that you must do this in-place without making a copy of the array.

"""





"""
You are given an integer array nums. You are initially positioned at the array's first index,
and each element in the array represents your maximum jump length at that position.
Return true if you can reach the last index, or false otherwise.
"""
def canJump(nums):
    farthest = 0
    
    # Iterate through the array
    for i in range(len(nums)):
        # If we can't reach the current index, return False
        if i > farthest:
            return False
        
        # Update the farthest position we can reach from the current position
        farthest = max(farthest, i + nums[i])
        
        # Early exit: if the farthest we can reach is already at or beyond the last index
        if farthest >= len(nums) - 1:
            return True
    
    # If we finish the loop, return True if the farthest is greater than or equal to the last index
    return farthest >= len(nums) - 1
