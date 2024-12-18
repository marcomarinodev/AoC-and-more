from typing import List
from collections import deque

def plusOne(digits: List[int]) -> List[int]:
    
    op_completed = False
    reminder = 0
    res = deque()
    
    for i in range(len(digits) - 1, -1, -1):
        if digits[i] == 9 and not op_completed:
            res.appendleft(0)
            reminder = 1
            continue
        
        if not op_completed:
            res.appendleft(digits[i] + 1)
            op_completed = True
            reminder = 0
            continue
        
        res.appendleft(digits[i])
        
    if reminder > 0:
        res.appendleft(reminder)
        
    return list(res)
        
print(plusOne([1,2,3]))
print(plusOne([4,3,2,1]))
print(plusOne([9]))
print(plusOne([8,9,9,9]))