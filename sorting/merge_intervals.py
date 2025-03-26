
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        stack = []
        
        def sort_criteria(interval):
            return interval[0]
        
        intervals.sort(key=sort_criteria)
        
        for interval in intervals:
            start, end = interval[0], interval[1]
            
            if len(stack) > 0 and start <= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1], end)
            else:
                stack.append([start, end])
        
        return stack
    
sol = Solution()
print(sol.merge([[1,3], [2,6], [15,18]]))
print(sol.merge([[1,2], [4,5], [2,2]]))
print(sol.merge([[1,4], [4,5]]))
print(sol.merge([[1,4]]))