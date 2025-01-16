#2 search a 2D matrix
from numpy import math

def search2DMatrix(matrix, target):

    ROWS, COLS = len(matrix), len(matrix[0])
    top, bot = 0, ROWS - 1


    while top <= bot:
        row = (top + bot) // 2

        if matrix[row][0] < target:
            bot = row - 1

        elif matrix[row][-1] > target:
            top = row + 1

        else:
            break

        if not (top <= bot):
            return False
        
        row = (top + bot) // 2

        l, r = 0, COLS - 1
        while l <= r:
            m = (l + r) // 2

            if target < matrix[row][m]:
                r = m - 1

            elif target > matrix[row][m]:
                l = m + 1

            else:
                return True
        return False

# 3 koko eating bananas
def minEatingBananas(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2
        for p in piles:
            hours += math.ceil(p / k)

        if hours <= h:
            res = min(res, hours)
            r = k - 1

        else:
            l = k + 1

    return res

# 4 min in roated sorted array

def findMin(nums):
    pass


# 5 time-based key-value store


#6 median of two sorted arrays



