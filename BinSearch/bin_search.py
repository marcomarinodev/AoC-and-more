
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def rec_search(nums: List[int], l: int, r: int, t: int) -> int:
            if l > r:
                return -1
            
            mid = int((l + r) / 2)
            
            if nums[mid] == t:
                return mid
            elif t > nums[mid]:
                return rec_search(nums, mid + 1, r, t)
            else:
                return rec_search(nums, l, mid - 1, t)
            
        return rec_search(nums, 0, len(nums) - 1, target)
            
        
sol = Solution()
nums1 = [-1,0,2,4,6,8]
nums2 = [-1,0,2,4,6,8]
nums3 = [-1,0,3,5,9,12]

print(sol.search(nums1, 4))
print(sol.search(nums2, 3))
print(sol.search(nums3, 9))
        