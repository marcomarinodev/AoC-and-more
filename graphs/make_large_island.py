from typing import List

class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)
        visited = set()
        islands_area = {}  # Map (r, c) -> island_id
        island_sizes = {}  # Map island_id -> area
        island_id = 2  # Start from 2 to distinguish from 1s in the grid

        # Step 1: Use DFS to find and store all islands
        def dfs(r, c):
            stack = [(r, c)]
            visited.add((r, c))
            area = 0
            
            while stack:
                cur_r, cur_c = stack.pop()
                area += 1
                islands_area[(cur_r, cur_c)] = island_id  # Assign island ID
                
                for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                    nr, nc = cur_r + dr, cur_c + dc
                    if (0 <= nr < n and 0 <= nc < n and 
                            grid[nr][nc] == 1 and (nr, nc) not in visited):
                        visited.add((nr, nc))
                        stack.append((nr, nc))

            return area

        # Step 2: Find all islands and store their sizes
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1 and (r, c) not in visited:
                    island_sizes[island_id] = dfs(r, c)
                    island_id += 1

        # Step 3: Try flipping each `0` and calculate the maximum possible island size
        max_island_size = max(island_sizes.values(), default=0)  # If no islands exist
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    seen_islands = set()
                    cur_area = 1  # The new 1 we add
                    
                    for dr, dc in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                        nr, nc = r + dr, c + dc
                        if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                            island_id = islands_area.get((nr, nc))
                            if island_id and island_id not in seen_islands:
                                seen_islands.add(island_id)
                                cur_area += island_sizes[island_id]

                    max_island_size = max(max_island_size, cur_area)

        return max_island_size