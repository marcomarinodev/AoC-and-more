
from typing import List
from collections import deque

INF = 2147483647

class Solution:
    def walls_and_gates(self, grid: List[List[int]]) -> None:
        to_visit, visited = self.get_gates_pos(grid)
        dirs = [(-1,0),(0,1),(1,0),(0,-1)]
        
        while to_visit:
            to_visit_row, to_visit_col = to_visit.pop()
            
            for dir in dirs:
                to_change_row = to_visit_row + dir[0]
                to_change_col = to_visit_col + dir[1]
                value_to_assign = grid[to_visit_row][to_visit_col] + 1
                
                if (0 <= to_change_row < len(grid) and
                    0 <= to_change_col < len(grid[0]) and
                    (to_change_row, to_change_col) not in visited and
                    grid[to_change_row][to_change_col] != -1 and
                    grid[to_change_row][to_change_col] > value_to_assign
                ):
                    grid[to_change_row][to_change_col] = value_to_assign
                    to_visit.appendleft((to_change_row, to_change_col))
                    
            visited.add((to_visit_row, to_visit_col))
                    
        print(grid)                
    
        return None
    
    def get_gates_pos(self, grid: List[List[int]]):
        gates_pos = deque()
        visited = set()
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 0:
                    gates_pos.append((i, j))
                    visited.add((i, j))
        
        return gates_pos, visited
    
sol = Solution()
graph1 = [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
graph2 = [
  [0,-1],
  [2147483647,2147483647]
]

sol.walls_and_gates(graph1)
sol.walls_and_gates(graph2)
