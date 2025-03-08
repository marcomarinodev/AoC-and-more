
class Solution:
    def fib(self, n: int) -> int:
        f0, f1 = 0, 1
        
        if n <= 1:
            return n
        
        for _ in range(n, 1, -1):
            tmp = f1
            f1 = f0 + f1
            f0 = tmp
            
        return f1
    
sol = Solution()

print(sol.fib(2))
print(sol.fib(3))
print(sol.fib(4))
print(sol.fib(10))