
from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        l, r = 0, 2
        op = 0
        
        while l < len(nums):
            if r >= len(nums):
                if nums[l] == 0:
                    return -1
                l += 1
                continue
            
            if nums[l] == 0:
                op += 1
                for i in range(l, r + 1):
                    nums[i] = (nums[i] + 1) % 2
            else:
                l += 1
                r += 1
                
        return op
    
sol = Solution()
print(sol.minOperations([0,1,1,1,0,0]))
            
        