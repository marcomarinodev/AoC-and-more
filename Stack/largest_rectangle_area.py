
from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # (index, height)
        heights_stack = []
        max_area = 0
        
        for i, h in enumerate(heights):
            
            last_popped_integer = i
            while heights_stack and h < heights_stack[-1][1]:
                # compute the area of the elements to pop
                width = i - heights_stack[-1][0]
                area = width * heights_stack[-1][1]
                max_area = max(max_area, area)
                
                # pop the element
                last_popped_integer = heights_stack[-1][0]
                heights_stack.pop(-1)
            
            heights_stack.append((last_popped_integer, h))
            
        for i, h in heights_stack:
            width = len(heights) - i
            area = width * h
            max_area = max(max_area, area)
        
        return max_area
                
        
sol = Solution()
print(sol.largestRectangleArea([2,1,5,6,2,3])) # 10
