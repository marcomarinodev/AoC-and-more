
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        visited: set[tuple[int, int]] = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == "1":
                    islands += 1
                    visited = self.dfs(grid, visited, (i, j))
        
        return islands
                    
    def dfs(self, grid: List[List[str]], visited: set[tuple[int, int]], start_pos) -> set[tuple[int, int]]:
        to_visit: List[tuple[int, int]] = []
        
        to_visit.append(start_pos)
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        
        while to_visit:
            cur_pos = to_visit.pop()
            
            for dir in dirs:
                # neighbor in the grid
                new_row_pos = cur_pos[0] + dir[0] 
                new_col_pos = cur_pos[1] + dir[1]
                
                if (0 <= new_row_pos < len(grid) and 
                    0 <= new_col_pos < len(grid[0]) and
                    (new_row_pos, new_col_pos) not in visited):
                    if grid[new_row_pos][new_col_pos] == "1":
                        to_visit.append((new_row_pos, new_col_pos))
            
            visited.add(cur_pos)
        
        return visited
    
sol = Solution()
grid1 = [
    ["0","1","1","1","0"],
    ["0","1","0","1","0"],
    ["1","1","0","0","0"],
    ["0","0","0","0","0"]
]

grid2 = [
    ["1","1","0","0","1"],
    ["1","1","0","0","1"],
    ["0","0","1","0","0"],
    ["0","0","0","1","1"]
  ]

print(sol.numIslands(grid1))
print(sol.numIslands(grid2))