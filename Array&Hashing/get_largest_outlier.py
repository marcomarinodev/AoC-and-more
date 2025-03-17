
from typing import List

class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        counts = {}
        overall_sum = 0
        res = -float("inf")
        
        for n in nums:
            counts[n] = counts.get(n, 0) + 1
            overall_sum += n
        
        for n in nums:
            # cur element is a possible outlier
            counts[n] -= 1
            expected_sum = (overall_sum - n) / 2
            
            if expected_sum in counts and counts[expected_sum] > 0:
                # cur element is for sure an outlier
                res = max(res, n)
            
            counts[n] += 1
        
        return res
            

sol = Solution()
print(sol.getLargestOutlier([2,3,5,10])) # 10
print(sol.getLargestOutlier([-2,-1,-3,-6,4])) # 4
print(sol.getLargestOutlier([1,1,1,1,1,5,5])) # 5