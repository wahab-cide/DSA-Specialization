from collections import defaultdict, List
# 1, has duplicates
def hasDuplicates(nums):
    hashSet = set()

    for num in nums:
        if num in hashSet:
            return True
    return False


# 2, is Anagram
def isAnagram(s, t):

    if len(s) != len(t):
        return False
    
    countS, countT = dict(), dict()
    
    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for c in countS:
        if countS[c] != countT.get(c, 0):
            return False
        
    return True


    # 3, two sum

    def twoSum(nums, target):

        compliment = dict()

        for i, n in enumerate(nums):
            diff = target - n

            if diff in compliment:
                return [compliment[diff], i]
            compliment[n] = i

#4 group anagrams

def groupAnagrams(strs: list[str]) -> list[list[str]]:

    from collections import defaultdict
    anagram_groups = defaultdict(list)
    
  
    for s in strs:

        sorted_str = ''.join(sorted(s))
        anagram_groups[sorted_str].append(s)
    
    return list(anagram_groups.values())

# 5 top k frequent num
def topKFrequent(nums, k):

    count = {}
    freq = [[] for i in range(len(nums) + 1)]


    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res
            

# 6 encode, decode

class Solution:
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes, res = [], ""
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            res += str(sz)
            res += ','
        res += '#'
        for s in strs:
            res += s
        return res

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes, res, i = [], [], 0
        while s[i] != '#':
            cur = ""
            while s[i] != ',':
                cur += s[i]
                i += 1
            sizes.append(int(cur))
            i += 1
        i += 1
        for sz in sizes:
            res.append(s[i:i + sz])
            i += sz
        return res


# 7 product except self

def productExceptSelf(self, nums: List[int]) -> List[int]:

        res = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1

        for i in range(len(nums) - 1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res

# 8 valid sudoku
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set)
        rows = defaultdict(set)
        squares = defaultdict(set)  

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if ( board[r][c] in rows[r]
                    or board[r][c] in cols[c]
                    or board[r][c] in squares[(r // 3, c // 3)]):
                    return False

                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r // 3, c // 3)].add(board[r][c])

        return True
    
# 9 longest consecutive sequence

def longestConsecutive(nums):

    numSet = set(nums)

    for num in nums:
        if (num - 1) not in numSet:
            length = 0
            while (num + length) in numSet:
                length += 1
            longest = max(longest, length)

    return longest




def mostUsedIp(connections):
    user_to_count = dict()

    for _, user in connections:
        if user not in user_to_count:
            user_to_count[user] = 0
        user_to_count[user] += 1

    most_shared_user = None
    for user, count in user_to_count.items():
        if not most_shared_user or count > user_to_count[most_shared_user]:
            most_shared_user = user
    return most_shared_user


def multiAccountCheating(users):
    uniqueLists = set()

    for _, ips in users:
        immutableList = tuple(sorted(ips))
        if immutableList in uniqueLists:
            return True
        uniqueLists.add(immutableList)
    return False





def longestSubstring(s):
    charPosition = dict()
    maxL = 0
    start = 0


    for pos, char in enumerate(s):
        if char in charPosition and charPosition[char] >= start:
            start = charPosition[char] + 1
        else:
            maxL = max(maxL, pos - start + 1)

        charPosition[char] = pos

    return maxL