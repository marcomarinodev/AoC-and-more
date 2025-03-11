
from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        
        # (temp, index)
        temp_stack = [(temperatures[-1], len(temperatures) - 1)]
        res = [0] * len(temperatures)
        
        for i in range(len(temperatures) - 2, -1, -1):
            while temp_stack and temperatures[i] >= temp_stack[-1][0]:
                temp_stack.pop(-1)
            
            if not temp_stack: 
                res[i] = 0
            elif temperatures[i] <= temp_stack[-1][0]:
                res[i] = temp_stack[-1][1] - i
            
            temp_stack.append((temperatures[i], i))
        
        return res
        
        
sol = Solution()
print(sol.dailyTemperatures([89,62,70,58,47,47,46,76,100,70])) # [8,1,5,4,3,2,1,1,0,0]
print(sol.dailyTemperatures([30, 38, 30, 36, 35, 40 ,28])) # [1, 4, 1, 2, 1, 0, 0]
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73])) # [1,1,4,2,1,1,0,0]
print(sol.dailyTemperatures([30,40,50,60])) # [1,1,1,0]
print(sol.dailyTemperatures([30,60,90])) # [1,1,0]
print(sol.dailyTemperatures([22,21,20])) # []
