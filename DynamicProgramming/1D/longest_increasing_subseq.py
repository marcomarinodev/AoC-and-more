
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        LIS = [1] * len(nums)
        
        for i in range(len(nums) - 1, -1, -1):
            
            max_j_LIS = 1
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    max_j_LIS = max(max_j_LIS, 1 + LIS[j])
            
            LIS[i] = max_j_LIS
        
        return max(LIS)
        
sol = Solution()
print(sol.lengthOfLIS([1,2,4,3])) # 3
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(sol.lengthOfLIS([0,1,0,3,2,3])) # 4
print(sol.lengthOfLIS([7,7,7,7,7,7,7])) # 1
