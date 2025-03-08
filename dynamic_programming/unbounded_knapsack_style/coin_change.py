from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0
        
        for i in range(1, amount + 1):
            for c in coins:
                if i - c >= 0: # if from my left amount I use a coin...
                    dp[i] = min(dp[i], dp[i -c] + 1)
        
        return dp[amount] if dp[amount] != float("inf") else - 1
            
        
sol = Solution()

print(sol.coinChange([1,2,5], 11))
print(sol.coinChange([2], 3))
print(sol.coinChange([1], 0))