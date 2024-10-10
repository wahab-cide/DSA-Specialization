"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""
def convert_to_military_time(time_str):
    # Extract the period (AM/PM) and split the time components
    period = time_str[-2:]
    time_components = time_str[:-2].split(":")
    
    # Handle cases where time_str is invalid
    if len(time_components) != 3:
        raise ValueError("Invalid time format")
    
    # Convert the hour to integer
    hour = int(time_components[0])
    
    # Handle AM/PM conversion
    if period == "AM":
        if hour == 12:
            hour = 0
    elif period == "PM":
        if hour != 12:
            hour += 12
    
    # Format the military time
    military_time = f"{hour:02}:{time_components[1]}:{time_components[2]}"
    return military_time

# Example usage:
time_str = "07:05:45PM"
print(convert_to_military_time(time_str))


"""
Given an array of integers, calculate the ratios of its elements that are positive,
negative, and zero. Print the decimal value of each fraction on a new line with  
places after the decimal.
"""

def num_ratios(arr):

    n = len(arr)
    positives = sum( 1 for x in arr if x > 0)
    negatives = sum(1 for x in arr if x < 0)
    zeros = sum(1 for x in arr if x == 0)


    positve_ratio = positives/ n
    negative_ratio = negatives/n
    zero_ratio = zeros/n

    print(f"{positve_ratio:.6f}")
    print(f"{negative_ratio:.6f}")
    print(f"{zero_ratio:.6f}")



"""
Given five positive integers, find the minimum and maximum values that can be calculated 
by summing exactly four of the five integers. Then print the respective minimum and 
maximum values as a single line of two space-separated long integers.

"""

def min_max_sum(arr):

    arr.sort

    max_sum = sum(arr[1:])
    min_sum = sum(arr[:4])

    print(f"{min_sum} {max_sum}")



"""
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.
"""

#extract the period
#split the components 

def convert_to_military_time(s):

    period = s[-2:]
    components = s[-2:].split(':')


    hour = int(components[0])

    if period == 'AM':
        if hour == 12:
            hour = 0
        else:
            hour += 12

    elif period == 'PM':
        if hour != 12:
            hour += 12

    military_time = f"{hour:02}:{components[1]}:{components[2]}"
    return military_time


"""
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

Input Format

The first line contains a single integer, n, the number of rows and columns in the square matrix arr.

[2,
[1, 2], 
[4, 5]
]

[3,
[1, 2, 3],
[4, 5, 6],
[7, 8, 9]

]
"""


"""
Given an array of  distinct integers, 
transform the array into a zig zag sequence 
by permuting the array elements. 
A sequence will be called a zig zag sequence 
if the first  elements in the sequence are in increasing 
order and the last  elements are in decreasing order, where . 
You need to find the lexicographically smallest zig zag sequence of the given array.
"""

def findZigZagSequence(a, n):
    # Sort the array in ascending order
    a.sort()
    
    # Find the middle index and swap it with the last element
    mid = (n - 1) // 2
    a[mid], a[n - 1] = a[n - 1], a[mid]
    
    # Reverse the second half of the array after the middle element
    st = mid + 1
    ed = n - 2
    while st <= ed:
        a[st], a[ed] = a[ed], a[st]
        st = st + 1
        ed = ed - 1
    
    # Print the zig zag sequence
    for i in range(n):
        if i == n - 1:
            print(a[i])
        else:
            print(a[i], end=' ')
    return

# Example usage
a = [1, 2, 3, 4, 5, 6, 7]
n = len(a)
findZigZagSequence(a, n)