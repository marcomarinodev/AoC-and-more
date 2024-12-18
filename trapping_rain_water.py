from typing import List

def trap(height: List[int]) -> int:
    if not height: return 0
    
    res = 0
    left, right = 0, len(height) - 1
    max_left = height[left]
    max_right = height[right]
    
    while left < right:
        if max_left < max_right:
            left += 1
            water_quantity = min(max_left, max_right) - height[left]
            res += max(0, water_quantity)
            max_left = max(max_left, height[left])
        else: 
            right -= 1
            water_quantity = min(max_left, max_right) - height[right]
            res += max(0, water_quantity)
            max_right = max(max_right, height[right])
    
    return res

print(trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(trap([4,2,0,3,2,5]))

