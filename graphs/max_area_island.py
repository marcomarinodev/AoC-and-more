from collections import deque
from typing import List

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        visited: set[tuple[int, int]] = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (i, j) not in visited and grid[i][j] == 1:
                    cur_area, visited = self.bfs(grid, visited, (i, j))
                    max_area = max(max_area, cur_area)
        
        return max_area
                
    def bfs(self, grid: List[List[int]], visited: set[tuple[int, int]], start_pos: tuple[int, int]):
        area = 0
        to_visit = deque()
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        to_visit.append(start_pos)
        visited.add(start_pos)  # Add to visited when enqueued
        
        while to_visit:
            cur_row_pos, cur_col_pos = to_visit.popleft()
            area += 1
            
            for dir in dirs:
                new_row_pos = cur_row_pos + dir[0]
                new_col_pos = cur_col_pos + dir[1]
                if (
                    0 <= new_row_pos < len(grid) and
                    0 <= new_col_pos < len(grid[0]) and
                    (new_row_pos, new_col_pos) not in visited and
                    grid[new_row_pos][new_col_pos] == 1
                ):
                    to_visit.append((new_row_pos, new_col_pos))
                    visited.add((new_row_pos, new_col_pos))  # Mark as visited here
        
        return (area, visited)


            
sol = Solution()
grid1 = [
  [0,1,1,0,1],
  [1,0,1,0,1],
  [0,1,1,0,1],
  [0,1,0,0,1]
]

grid2 = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]

print(sol.maxAreaOfIsland(grid1))
print(sol.maxAreaOfIsland(grid2))