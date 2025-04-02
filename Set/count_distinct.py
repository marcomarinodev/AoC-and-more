
from typing import List

class Solution:
    def countDistinct(self, nums: List[int], k: int, p: int) -> int:
        res = set()
        N = len(nums)

        for i in range(N):
            count = 0

            for j in range(i, N):
                if nums[j] % p == 0:
                    count += 1
                if count > k:
                    break
                
                res.add(tuple(nums[i:j + 1]))

        return len(res)
    
sol = Solution()
print(sol.countDistinct([2,3,3,2,2], 2, 2)) # 11
print(sol.countDistinct([1,2,3,4], 4, 1)) # 10
                