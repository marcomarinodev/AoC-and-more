
from typing import List
from collections import defaultdict

class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        count = defaultdict(int)
        res = []
        
        for num in nums:
            for el in num:
                count[el] += 1
        
        for k, v in count.items():
            if v == len(nums):
                res.append(k)
        
        res.sort()
        return res
    
sol = Solution()
print(sol.intersection([[3,1,2,4,5],[1,2,3,4],[3,4,5,6]]))
print(sol.intersection([[1,2,3],[4,5,6]]))
