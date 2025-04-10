
from typing import List

class Solution:
    
    def circularArrayLoop(self, nums: List[int]) -> bool:
        visited = set()
        
        def get_next(index, dir):
            next_index = (index + nums[index]) % len(nums)
            next_dir = 1 if nums[next_index] > 0 else -1
            
            # -1 if some of the properties to check if there's a cycle fails
            if dir != next_dir:
                return -1 # invalid from the problem property
        
            # self cycle is not a cycle for the problem
            if index == next_index:
                return -1
            
            return next_index
        
        for i in range(len(nums)):
            if i in visited:
                continue
            
            sp = fp = i
            cur_dir = 1 if nums[i] > 0 else -1
            
            while True:
                visited.add(sp)
                visited.add(fp)
                sp = get_next(sp, cur_dir)
                fp = get_next(fp, cur_dir)
                
                if sp == -1 or fp == -1:
                    break
                
                fp = get_next(fp, cur_dir)
                
                if fp == -1:
                    break
                
                if sp == fp:
                    return True
        
        return False