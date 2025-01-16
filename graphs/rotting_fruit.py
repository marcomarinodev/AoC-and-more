from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        to_visit = deque()
        minutes = 0
        fruits_num, rotten_fruits_num = 0, 0
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    continue
                fruits_num += 1
                if grid[i][j] == 2:
                    rotten_fruits_num += 1
                    to_visit.append((i, j))
                    
        while to_visit:
            popped_rotten_fruits = []
            while to_visit:
                popped_rotten_fruits.append(to_visit.pop())
            
            new_rotted = False
            for rotten_fruit_pos in popped_rotten_fruits:
                cur_row, cur_col = rotten_fruit_pos[0], rotten_fruit_pos[1]
                for dir in dirs:
                    new_row, new_col = cur_row + dir[0], cur_col + dir[1]
                    if (
                        0 <= new_row < len(grid) and 0 <= new_col < len(grid[new_row]) and
                        grid[new_row][new_col] == 1
                    ):
                        grid[new_row][new_col] = 2
                        rotten_fruits_num += 1
                        to_visit.appendleft((new_row, new_col))
                        new_rotted = True

            if new_rotted:
                minutes += 1
        
        return minutes if rotten_fruits_num == fruits_num else -1
        
        
sol = Solution()
grid1 = [[1,1,0],[0,1,1],[0,1,2]]
grid2 = [[1,0,1],[0,2,0],[1,0,1]]

print(sol.orangesRotting(grid1))
print(sol.orangesRotting(grid2))
