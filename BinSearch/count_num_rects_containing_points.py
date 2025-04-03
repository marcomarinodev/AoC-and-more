
from typing import List
from collections import defaultdict

class Solution:
    
    # returns the smallest index having value bigger than x in array lengths
    def bin_search(self, lengths, x):
        l = 0
        r = len(lengths) - 1
        ans = len(lengths)
        
        while l <= r:
            m = l + (r - l) // 2
            
            if lengths[m] >= x:
                ans = m
                r = m - 1
            else:
                l = m + 1
        
        return ans
    
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        heights = defaultdict(list)
        count = []
        
        for l, h in rectangles:
            heights[h].append(l)
        
        for k, v in heights.items():
            v.sort()
        
        for x, y in points:
            rects_count = 0
            # find rectangles having height greater or equal 
            # than this current point's height
            for j in range(y, 101):
                if j in heights:
                    # do bin search to get how many lengths
                    # are greater or equal than x for this given height j
                    rects_count += len(heights[j]) - self.bin_search(heights[j], x)
            
            count.append(rects_count)

        return count
    
sol = Solution()
print(sol.countRectangles([[1,2],[2,3],[2,5]], [[2,1],[1,4]])) # [2, 1]
print(sol.countRectangles([[1,1],[2,2],[3,3]], [[1,3],[1,1]])) # [1, 3]
