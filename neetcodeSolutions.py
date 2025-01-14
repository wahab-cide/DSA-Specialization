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

def groupAnagrams(strs):
    pass