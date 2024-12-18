from collections import deque 
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    l = r = 0
    q = deque() # we store the positions of the elements in nums that are in the sliding window
    output = []
    
    while r < len(nums):
        
        # popping all the elements smaller then the current pointed element
        while q and nums[r] > nums[q[-1]]:
            q.pop()
        q.append(r)
        
        if l > q[0]: # popping the left-most element in the deque as it is not in the window anymore
            q.popleft()
            
        if r + 1 >= k:
            output.append(nums[q[0]])
            l += 1 # move the left pointer only when i have a sliding window of size k
        
        r += 1 # always move the right-most index
    
    return output   
        