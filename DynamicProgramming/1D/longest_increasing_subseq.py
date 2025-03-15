
from typing import List

class Solution:
    
    # this takes O(N^2)
    # def lengthOfLIS(self, nums: List[int]) -> int:
        
    #     LIS = [1] * len(nums)
        
    #     for i in range(len(nums) - 1, -1, -1):
            
    #         max_j_LIS = 1
    #         for j in range(i + 1, len(nums)):
    #             if nums[i] < nums[j]:
    #                 max_j_LIS = max(max_j_LIS, 1 + LIS[j])
            
    #         LIS[i] = max_j_LIS
        
    #     return max(LIS)
        
    def bin_search(self, t: int, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1
        
        while l != r:
            mid = l + (r - l) // 2
            if t > arr[mid]:
                l = mid + 1
            else:
                r = mid
        
        return l
        
        
    def lengthOfLIS(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        increasing_subseq = [nums[0]]
        
        for n in nums:
            if n > increasing_subseq[-1]:
                increasing_subseq.append(n)
                continue
            
            index_to_replace = self.bin_search(n, increasing_subseq)
            
            increasing_subseq[index_to_replace] = n
        
        return len(increasing_subseq)
    
sol = Solution()
print(sol.lengthOfLIS([1,2,4,3])) # 3
print(sol.lengthOfLIS([10,9,2,5,3,7,101,18])) # 4
print(sol.lengthOfLIS([0,1,0,3,2,3])) # 4
print(sol.lengthOfLIS([7,7,7,7,7,7,7])) # 1
