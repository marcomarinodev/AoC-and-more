
from typing import List
from collections import deque

def read_mat(filename: str) -> List[List[str]]:
    res = []
    with open(filename) as file:
        for line in file:
            res_row = []
            for c in line[:-1]:
                res_row.append(c)
            res.append(res_row)
    return res

def dfs(mat: List[List[str]], start_pos: tuple[int, int], visited: set) -> int:
    perim = 0
    to_visit = deque()
    area = 0
    
    to_visit.append(start_pos)
    
    while to_visit:
        cur_row, cur_col = to_visit.popleft()
        cur_v = mat[cur_row][cur_col]
        
        if (cur_row, cur_col) in visited:
            continue
        
        visited.add((cur_row, cur_col))
        area += 1
        directions = [(1,0),(-1,0),(0,1),(1,0)]
        
        for dr, dc in directions:
            new_row = cur_row + dr
            new_col = cur_col + dc
            
            if not(0 <= new_row < len(mat) and 0 <= new_col < len(mat[0])):
                perim += 1
            elif mat[new_row][new_col] != cur_v:
                perim += 1
            else: to_visit.appendleft((new_row, new_col))
        
    return area * perim

def solve1(mat: List[List[str]]) -> int:
    visited = set()
    res = 0

    for r in range(len(mat)):
        for c in range(len(mat[r])):
            if (r, c) not in visited:
                res += dfs(mat, (r, c), visited)
    return res


print(solve1(read_mat("input.txt")))