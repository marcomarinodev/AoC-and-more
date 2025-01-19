from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        
        if not intervals:
            return [newInterval]
        
        def bin_search(intervals: List[List[int]], newInterval: List[int], l: int, r: int) -> int:
            # Base case: single element left
            if l == r:
                return l if newInterval[0] <= intervals[l][0] else l + 1

            mid = l + (r - l) // 2

            if newInterval[0] == intervals[mid][0]:
                return mid  # If they are equal, return current position
            elif newInterval[0] > intervals[mid][0]:
                if mid == r:  # Handle edge case
                    return mid + 1
                return bin_search(intervals, newInterval, mid + 1, r)
            else:  # newInterval[0] < intervals[mid][0]
                if mid == l:  # Handle edge case
                    return mid
                return bin_search(intervals, newInterval, l, mid)
            
        insert_pos = bin_search(intervals, newInterval, 0, len(intervals) - 1)
        intervals.insert(insert_pos, newInterval)
        
        for interval in intervals:
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
                continue
            
            res[-1][1] = max(res[-1][1], interval[1])
        
        return res
        
    
sol = Solution()
i1 = [[1,3],[4,6]]
i2 = [[1,2],[3,5],[9,10]]
i3 = [[1,2],[3,5],[6,7],[8,10],[12,16]]

print(sol.insert(i1, [2,5]))
print(sol.insert(i2, [6,7]))
print(sol.insert(i3, [4,8]))

"""
[[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]


[1,3,6,7,8,9,10], 5



[[1,2],[3,5],[4,8],[6,7],[8,10],[12,16]]

[[1,2],[3,10],[12,16]]

"""
