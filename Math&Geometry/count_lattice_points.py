
from typing import List

class Solution:
    
    def is_lattice(self, x, y, xc, yc, r) -> bool:
        return (x - xc)**2 + (y - yc)**2  <= r**2
    
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        lattice_points = set()
        
        for x, y, r in circles:
            for i in range(x - r, x + r + 1):
                for j in range(y - r, y + r + 1):
                    if self.is_lattice(i, j, x, y, r):
                        lattice_points.add((i, j))
        
        return len(lattice_points)
    
sol = Solution()

print(sol.countLatticePoints([[2,2,1]])) # 5
print(sol.countLatticePoints([[2,2,2],[3,4,1]])) # 16
