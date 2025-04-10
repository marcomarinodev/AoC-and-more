
from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return -1
        
        res = float("-inf")
        _sum = 0
        
        for r in range(len(nums)):
            _sum += nums[r]
            
            if _sum < 0:
                res = max(res, _sum)
                _sum = 0
                continue
                
            res = max(res, _sum)
        
        return res
    
sol = Solution()

print(sol.maxSubArray([-2,1,-3,4,-1,2,1,-5,4])) # 6
print(sol.maxSubArray([1])) # 1
print(sol.maxSubArray([5,4,-1,7,8])) # 23
