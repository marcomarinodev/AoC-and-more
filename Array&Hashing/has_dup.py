
from typing import List

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = {}
        
        for n in nums:
            if n in nums_dict:
                return True
            
            nums_dict[n] = n
            
        return False
        
