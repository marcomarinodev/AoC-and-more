
from typing import List
import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        k = float('-inf')
        for p in piles:
            k = max(k, p)
            
        def time_taken(piles: List[int], try_k: int) -> int:
            hours_taken = 0
            
            for i in range(len(piles)):
                hours_taken += math.ceil(piles[i] / try_k)
                
            return hours_taken
        
        def rec_search(piles: List[int], h: int, l: int, r: int, min_k: int) -> int:
            if l > r:
                return min_k
            
            try_k = l + (r - l) // 2
            hours_taken = time_taken(piles, try_k)
            
            # print(f"trying with k={try_k}, hours taken={hours_taken}")
            
            if hours_taken > h:
                # print(f"{try_k} doesn't complete in time")
                return rec_search(piles, h, try_k + 1, r, min_k)
            
            return rec_search(piles, h, l, try_k - 1, try_k)
            
        return rec_search(piles, h, 1, k, k)
    
sol = Solution()
p1 = [1,4,3,2]
p2 = [25,10,23,4]

print(sol.minEatingSpeed(p1, 9)) # 2
print(sol.minEatingSpeed(p2, 4)) # 25
