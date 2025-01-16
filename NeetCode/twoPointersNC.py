# 1 is plaindrome


def isPalindrome(s):

    newStr = ""

    for c in s:
        if c.isalnum():
            newStr += c.lower()

    return newStr == newStr[::-1]

#two pointers
def isPalindrome2(s):
    
    
    l, r = 0, len(s) - 1

    while l < r:
        while l < r and not isalNum(s[l]):
            l += 1

        while r > l and not isalNum(s[r]):
            r -= 1


        if s[l].lower() != s[r].lower():
            return False
        
    return True




def isalNum(c):

    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


# 2 two sum II

def twosumII(numbers, target):

    l, r = 0, len(numbers) - 1

    while l < r:

        currSum = numbers[l] + numbers[r]

        if currSum == target:
            return [l + 1, r + 1]
        elif currSum < target:
            l += 1
        else:
            r -= 1


# 3 three sum
def threeSum(nums):

    res = []
    nums.sort()

    for i, a in enumerate(nums):
        if i > 0 and a == nums[i - 1]:
            continue

        l, r = i + 1, len(nums)

        while l < r:
            threesum = a + nums[l] + nums[r]

            if threesum == 0:
                res.append([a, nums[l], nums[r]])
            elif threesum < 0:
                l += 1
            else:
                r -= 1
                l += 1

                while nums[l] == nums[l - 1] and l < r:
                    l += 1
    return res


# 4 container with most water

def maxArea(heights):

    res = 0

    l, r = 0, len(heights) - 1

    while l < r:
        area = (r - l) * min(heights[l], heights[r])

        res = max(res, area)

        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res

# 5 trapping rain water

def trap(height):

    if not height: return 0

    l, r = 0, len(height)
    lMax, rMax = height[l], height[r]
    res = 0

    while l < r:

        if lMax < rMax:
            l += 1
            lMax = max(lMax, height[l])
            res += lMax - height[[l]]
        
        else:
            r -= 1
            rMax = max(rMax, height[r])
            res += rMax - height[r]

    return res



