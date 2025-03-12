
from typing import List

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        l = r = 0
        res = -float("inf")
        cur_sum = 0
        
        for r in range(len(nums)):
            cur_sum += nums[r]
            
            if r - l + 1 > k:
                res = max(res, (cur_sum - nums[r]) / k)
                cur_sum -= nums[l]
                l += 1
            
            if r - l + 1 == k:
                res = max(res, cur_sum / k)
        
        return res
            
        
sol = Solution()
print(sol.findMaxAverage([1,12,-5,-6,50,3], 4)) # 12.75
print(sol.findMaxAverage([5], 1)) # 5.0