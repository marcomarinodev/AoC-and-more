
from typing import List
from collections import deque

def read_mat(filename: str) -> List[List[int]]:
    mat = []
    with open(filename) as file:
        for line in file:
            mat.append(list(map(int, line[:-1])))
    return mat

def solve(input_mat: List[List[int]]) -> int:
    res = 0
    zeros_pos = []
    
    for i in range(len(input_mat)):
        for j in range(len(input_mat[i])):
            if input_mat[i][j] == 0:
                zeros_pos.append((i, j))
    
    for zero_pos in zeros_pos:
        score = 0
        visited = set()
        to_visit = deque([zero_pos])
        
        while to_visit:
            cur_pos = to_visit.pop()
            cur_pos_row, cur_pos_col = cur_pos[0], cur_pos[1]
            cur_val = input_mat[cur_pos_row][cur_pos_col]
            
            if cur_val == 9:
                score += 1
            
            for dir in [(-1,0),(0,1),(1,0),(0,-1)]:
                if 0 <= cur_pos_row + dir[0] < len(input_mat) and 0 <= cur_pos_col + dir[1] < len(input_mat):
                    candidate_to_visit = input_mat[cur_pos_row + dir[0]][cur_pos_col + dir[1]]
                    candidate_to_visit_pos = (cur_pos_row + dir[0], cur_pos_col + dir[1])
                    if candidate_to_visit - cur_val == 1 and candidate_to_visit_pos not in visited:
                        to_visit.append(candidate_to_visit_pos)
            
            visited.add(cur_pos)
        
        res += score
    
    return res

def solve1(input_mat: List[List[int]]) -> int:
    
    res = 0
    zeros_pos = []
    
    for i in range(len(input_mat)):
        for j in range(len(input_mat[i])):
            if input_mat[i][j] == 0:
                zeros_pos.append((i, j))
    
    for zero_pos in zeros_pos:
        score = 0
        visited = set()
        to_visit = deque([zero_pos])
        
        while to_visit:
            cur_pos = to_visit.pop()
            cur_pos_row, cur_pos_col = cur_pos[0], cur_pos[1]
            cur_val = input_mat[cur_pos_row][cur_pos_col]
            
            if cur_val == 9:
                score += 1
            
            for dir in [(-1,0),(0,1),(1,0),(0,-1)]:
                if 0 <= cur_pos_row + dir[0] < len(input_mat) and 0 <= cur_pos_col + dir[1] < len(input_mat):
                    candidate_to_visit = input_mat[cur_pos_row + dir[0]][cur_pos_col + dir[1]]
                    candidate_to_visit_pos = (cur_pos_row + dir[0], cur_pos_col + dir[1])
                    if candidate_to_visit - cur_val == 1 and (candidate_to_visit == 9 or candidate_to_visit_pos not in visited):
                        to_visit.appendleft(candidate_to_visit_pos)
            
            visited.add(cur_pos)
        
        res += score
    
    return res

print(solve(read_mat("sample.txt")))
print(solve(read_mat("sample2.txt")))
print(solve(read_mat("input.txt")))

print("------------")
print(solve1(read_mat("sample3.txt")))
print(solve1(read_mat("sample4.txt")))
print(solve1(read_mat("input.txt")))
            