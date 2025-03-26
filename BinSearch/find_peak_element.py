
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        def bin_search(l: int, r: int) -> int:
            if l == r:
                return l
            
            mid = l + (r - l) // 2
            
            left_val = float("-inf")
            right_val = float("-inf")
            
            if mid - 1 >= 0:
                left_val = nums[mid - 1]
            
            if mid + 1 < len(nums):
                right_val = nums[mid + 1]
                
            if nums[mid] > left_val and nums[mid] > right_val:
                return mid

            if nums[mid] < left_val:
                return bin_search(l, mid - 1)
            
            if nums[mid] < right_val:
                return bin_search(mid + 1, r)
            
        return bin_search(0, len(nums) - 1)
    
sol = Solution()

print(sol.findPeakElement([1,2]))
print(sol.findPeakElement([1,2,3,1]))
print(sol.findPeakElement([1,2,1,3,5,6,4]))
