from collections import defaultdict
"""
Given an array nums of distinct positive integers, return the number of tuples (a, b, c, d) 
such that a * b = c * d where a, b, c, and d are elements of nums, and a != b != c != d.

"""

class Solution:
    from collections import defaultdict

    def tupleSameProduct(self, nums):
        n = len(nums)
        product_map = defaultdict(list)
        
       
        for i in range(n):
            for j in range(n):
                if i != j:
                    product = nums[i] * nums[j]
                    product_map[product].append((i, j))
        
        total = 0
        
        
        for product, pairs in product_map.items():
            
            unique_pairs = set()
            for i, j in pairs:
                a, b = nums[i], nums[j]
                if a < b:
                    unique_pairs.add((a, b))
                else:
                    unique_pairs.add((b, a))
            unique_pairs = list(unique_pairs)
            m = len(unique_pairs)
            
          
            count = 0
            for s_idx in range(m):
                s = unique_pairs[s_idx]
                s_elements = set(s)
                for t_idx in range(m):
                    if s_idx != t_idx:
                        t = unique_pairs[t_idx]
                        t_elements = set(t)
                        if s_elements.isdisjoint(t_elements):
                            count += 1
            
            total += count * 4
        
        return total

   