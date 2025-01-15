# 22 categories


#remove duplicates  I 26
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
