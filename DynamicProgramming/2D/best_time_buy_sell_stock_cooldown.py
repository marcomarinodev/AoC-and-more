
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # (index, buy/sell) -> max profit
        dp = {}
        
        def dfs(index: int, buying: bool) -> int:
            # base condition
            if index > len(prices) - 1:
                return 0
            
            # check in dp
            if (index, buying) in dp:
                return dp[(index, buying)]
            
            cooldown_max_profit = dfs(index + 1, buying)
            if buying:
                # if in buying state, we can buy or cooldown
                buy_max_profit = -prices[index] + dfs(index + 1, not buying)    
                dp[(index, buying)] = max(buy_max_profit, cooldown_max_profit)
            else:
                sell_profit = prices[index] + dfs(index + 2, not buying)
                dp[(index, buying)] = max(sell_profit, cooldown_max_profit)
            
            return dp[(index, buying)]
                
        return dfs(0, True)
    
