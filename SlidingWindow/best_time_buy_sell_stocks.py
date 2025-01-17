
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_p = 0
        cur_min = float('inf')
        
        for p in prices:
            if p < cur_min:
                cur_min = p
                continue
            
            max_p = max(max_p, p - cur_min)
            
        return max_p
    
sol = Solution()
p1 = [10,1,5,6,7,1]
p2 = [10,8,7,5,2]

print(sol.maxProfit(p1)) # 6
print(sol.maxProfit(p2)) # 0