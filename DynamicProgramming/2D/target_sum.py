from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:

        dp = {} # (index, total) -> # of ways

        def backtrack(index: int, total: int) -> int:
            if index == len(nums):
                return 1 if total == target else 0
            
            if (index, total) in dp:
                return dp[(index, total)]
            
            dp[(index, total)] = (backtrack(index + 1, total + nums[index]) 
                                    + backtrack(index + 1, total - nums[index]))
            
            return dp[(index, total)]
            
        return backtrack(0, 0)
        
sol = Solution()
