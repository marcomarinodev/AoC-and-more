
from typing import List

class Solution:
    def occurrencesOfElement(self, nums: List[int], queries: List[int], x: int) -> List[int]:
        occurrences = []
        res = []
        
        for i in range(len(nums)):
            if nums[i] == x:
                occurrences.append(i)
        
        for q in queries: 
            if q - 1 < len(occurrences):
                res.append(occurrences[q - 1])
            else:
                res.append(-1)
        
        return res
    
sol = Solution()
print(sol.occurrencesOfElement([1,3,1,7], [1,3,2,4], 1))
print(sol.occurrencesOfElement([1,2,3], [10], 5))
