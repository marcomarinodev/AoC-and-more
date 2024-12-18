from typing import List

def longestConsecutive(self, nums: List[int]) -> int:
    nums_set = set(nums)
    res = 0

    for num in nums_set:
        if num - 1 not in nums_set: # it's the start of a sequence
            current_seq_len = 1
            i = num
            while i + 1 in nums_set:
                current_seq_len += 1
                i += 1
            
            res = max(res, current_seq_len)
    return res