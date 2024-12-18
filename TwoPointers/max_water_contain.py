from typing import List

def maxArea(height: List[int]) -> int:
    l, r = 0, len(height) - 1
    max_water = 0
    
    while l < r:
        cur_water = min(height[l], height[r]) * (r - l)
        max_water = max(max_water, cur_water)
        
        if height[l] < height[r]: l += 1
        else: r -= 1
    
    return max_water

print(maxArea([1,8,6,2,5,4,8,3,7])) # 49
print(maxArea([1,1])) # 1
        