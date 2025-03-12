
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def find_deflection(l: int, r: int) -> int:
            if l == r:
                return l
            
            mid = l + (r - l) // 2
            
            if nums[mid] > nums[r]:
                return find_deflection(mid + 1, r)
            else:
                return find_deflection(l, mid)
        
        def bin_search(l: int, r: int) -> int:
            if l > r:
                return -1
            
            mid = l + (r - l) // 2
            
            if nums[mid] == target:
                return mid
            
            if nums[mid] < target:
                return bin_search(mid + 1, r)
            else:
                return bin_search(l, mid - 1)
        
        if not nums:
            return -1
        
        d_index = find_deflection(0, len(nums) - 1)
        
        if nums[d_index] <= target <= nums[-1]:
            return bin_search(d_index, len(nums) - 1)
        else:
            return bin_search(0, d_index - 1)
        
sol = Solution()
