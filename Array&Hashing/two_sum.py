from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    to_sum_dict = {}
    
    for i in range(len(nums)):
        diff = target - nums[i]
        if diff in to_sum_dict:
            return [to_sum_dict[diff], i]
        to_sum_dict[nums[i]] = i
    
    return []

        