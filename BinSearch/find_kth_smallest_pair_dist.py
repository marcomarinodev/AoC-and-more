from typing import List

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        def sliding_window_helper(dist):
            # count total num of pairs
            # with diff <= dist
            l = 0
            res = 0
            for r in range(len(nums)):
                while nums[r] - nums[l] > dist:
                    l += 1
                res += r - l
            return res

        l, r = 0, max(nums)

        while l < r:
            m = l + ((r - l) // 2)
            num_pairs = sliding_window_helper(m)
            if num_pairs >= k:
                r = m
            else:
                l = m + 1
        
        return r