from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = {}
        range_days = [1,7,30]
        
        for i in range(len(days) - 1, -1, -1):
            dp[i] = float("inf")
            
            for num_days, cost in zip(range_days, costs):
                k = i
                while k < len(days) and days[k] < days[i] + num_days:
                    k += 1
                dp[i] = min(dp[i], cost + dp.get(k, 0))
                
        return dp[0]
            
        
sol = Solution()

print(sol.mincostTickets(
    [1,4,6,7,8,20],
    [2,7,15]
)) # 11

print(sol.mincostTickets(
    [1,2,3,4,5,6,7,8,9,10,30,31],
    [2,7,15]
)) # 17

