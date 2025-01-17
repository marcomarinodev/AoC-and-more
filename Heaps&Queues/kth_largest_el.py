
from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)
            
        return min_heap[0]
    
sol = Solution()
p1 = [2,3,1,5,4]
p2 = [2,3,1,1,5,5,4]

print(sol.findKthLargest(p1, 2))
print(sol.findKthLargest(p2, 3))
