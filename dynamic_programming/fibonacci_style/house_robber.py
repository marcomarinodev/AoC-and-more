from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[1], dp[0])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], dp[i - 2] + nums[i])
            
        return dp[-1]
    
sol = Solution()

print(sol.rob([1,2,3,1]))
print(sol.rob([2,7,9,3,1]))
