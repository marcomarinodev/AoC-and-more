
from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        cur_num = 0
        
        for num in nums:
            if count == 0:
                cur_num = num
            
            if num != cur_num:
                count -= 1
            else:
                count += 1
        
        return cur_num

sol = Solution()