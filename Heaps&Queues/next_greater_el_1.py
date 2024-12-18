from typing import List
from collections import deque, defaultdict

def nextGreaterElement(nums1: List[int], nums2: List[int]) -> List[int]:
    
    monotonic_stack = deque()
    next_greater_el_dict = defaultdict(lambda: -1)
    res = []
    
    for num in nums2:
        while monotonic_stack and monotonic_stack[-1] < num:
            next_greater_el_dict[monotonic_stack[-1]] = num
            monotonic_stack.pop()
            
        monotonic_stack.append(num)

    for num in nums1:
        res.append(next_greater_el_dict[num])
    
    return res

print(nextGreaterElement([4,1,2], [1,3,4,2]))
print(nextGreaterElement([2,4], [1,2,3,4]))
print(nextGreaterElement([], []))
print(nextGreaterElement([0,1,2], [2,0,1,3]))
