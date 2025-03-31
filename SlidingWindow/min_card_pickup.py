
from typing import List

class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        if len(cards) <= 1:
            return -1
        
        min_res = float("inf")
        last_occurrence_dict = {}
        
        for i in range(len(cards)):
            if cards[i] in last_occurrence_dict:
                min_res = min(min_res, i - last_occurrence_dict[cards[i]] + 1)
            
            last_occurrence_dict[cards[i]] = i

        return min_res if min_res != float("inf") else -1
            

sol = Solution()
print(sol.minimumCardPickup([2,3,4,3,4,7])) # 2
print(sol.minimumCardPickup([3,4,2,3,4,7])) # 4
print(sol.minimumCardPickup([1,0,5,3])) # -1
