
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n
        
        for _ in range(m - 1):
            new_row = [1] * n
            for j in range(n - 2, -1, -1):
                new_row[j] = new_row[j + 1] + row[j] # from right + from bottom
            row = new_row
            
        return row[0]
        
sol = Solution()
print(sol.uniquePaths(3, 7)) # 28
print(sol.uniquePaths(3, 2)) # 3

# O(n * m) time
# O(n) space