from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        def helper(l: int, r: int, go_right: bool) -> int:
            if r - l <= 0:
                return -1

            mid = int(l + (r - l) / 2)
            
            if mid - 1 >= 0 and nums[mid] < nums[mid - 1]:   
                return nums[mid]
            
            if mid + 1 < len(nums) and nums[mid] > nums[mid + 1]:
                return nums[mid + 1]
            
            if go_right:
                return helper(mid + 1, r, go_right=go_right)
            
            return helper(l, mid - 1, go_right=go_right)
        
        go_right_res = helper(0, len(nums) - 1, True)
        go_left_res = helper(0, len(nums) - 1, False)
        
        if go_right_res >= 0:
            return go_right_res
        
        if go_left_res >= 0:
            return go_left_res
        
        return nums[0]
        
sol = Solution()

print(sol.findMin([3,4,5,6,1,2]))
print(sol.findMin([4,5,0,1,2,3]))
print(sol.findMin([4,5,6,7]))
print(sol.findMin([2,1]))
print(sol.findMin([3,1,2]))