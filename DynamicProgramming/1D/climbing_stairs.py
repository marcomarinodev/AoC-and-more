
class Solution:
    def climbStairs(self, n: int) -> int:
        # start from n - 1
        dp = [0] * (n) + [1] + [0]
        
        for i in range(n - 1, -1, -1):
            left_count = dp[i + 1]
            right_count = dp[i + 2]
            
            dp[i] = left_count + right_count
        
        return dp[0]
        
    def climbStairsConstantSpace(self, n: int) -> int:
        one_branch, two_branch = 1, 0
        
        for _ in range(n - 1, -1, -1):
            left_count = one_branch
            right_count = two_branch
            
            prev_one_branch = one_branch
            one_branch = left_count + right_count
            two_branch = prev_one_branch
            
        return one_branch
        
sol = Solution()

print(sol.climbStairsConstantSpace(2))
print(sol.climbStairsConstantSpace(3))
print(sol.climbStairsConstantSpace(5))