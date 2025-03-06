from typing import List

class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        max_res = 0
        cur_size = 0
        
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        
        for bt in boxTypes:
            for _ in range(bt[0]):
                if cur_size + 1 <= truckSize:
                    max_res += bt[1]
                    cur_size += 1
                else:
                    return max_res
                
        return max_res
    
sol = Solution()

in1, ts1 = [[1,3],[2,2],[3,1]], 4
in2, ts2 = [[5,10],[2,5],[4,7],[3,9]], 10

print(sol.maximumUnits(in1, ts1))
print(sol.maximumUnits(in2, ts2))