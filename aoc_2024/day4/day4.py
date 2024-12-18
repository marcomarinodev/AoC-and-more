from typing import List

def read_input(filename: str) -> List[List[str]]:
    res = []
    with open(filename) as file:
        for line in file:
            res.append(list(line.strip()))  # Fix: Split each line into a list of characters
    return res

def solve1(input_mat: List[List[str]]) -> int:
    res = 0
    
    for i in range(len(input_mat)):
        for j in range(len(input_mat[i])):
            if input_mat[i][j] == "M":
                # from left to right
                if j - 1 >= 0 and input_mat[i][j - 1] == "X":
                    if j + 2 < len(input_mat[i]) and input_mat[i][j+1] == "A" and input_mat[i][j+2] == "S":
                        res += 1
                
                # from right to left
                if j + 1 < len(input_mat[i]) and input_mat[i][j + 1] == "X":
                    if j - 2 >= 0 and input_mat[i][j-1] == "A" and input_mat[i][j-2] == "S":
                        res += 1
                        
                # from top to bottom
                if i - 1 >= 0 and input_mat[i-1][j] == "X":
                    if i + 2 < len(input_mat) and input_mat[i+1][j] == "A" and input_mat[i+2][j] == "S":
                        res += 1
                        
                # from bottom to top
                if i + 1 < len(input_mat) and input_mat[i+1][j] == "X":
                    if i - 2 >= 0 and input_mat[i-1][j] == "A" and input_mat[i-2][j] == "S":
                        res += 1
                
                # from top left
                if i - 1 >= 0 and j - 1 >= 0 and input_mat[i-1][j-1] == "X":
                    if i + 2 < len(input_mat) and j + 2 < len(input_mat[i]):
                        if input_mat[i+1][j+1] == "A" and input_mat[i+2][j+2] == "S":
                            res += 1
                            
                # from top right
                if i - 1 >= 0 and j + 1 < len(input_mat[i]) and input_mat[i-1][j+1] == "X":
                    if i + 2 < len(input_mat) and j - 2 >= 0:
                        if input_mat[i+1][j-1] == "A" and input_mat[i+2][j-2] == "S":
                            res += 1
                
                # from bottom left
                if i + 1 < len(input_mat) and j - 1 >= 0 and input_mat[i+1][j-1] == "X":
                    if i - 2 >= 0 and j + 2 < len(input_mat[i]):
                        if input_mat[i-1][j+1] == "A" and input_mat[i-2][j+2] == "S":
                            res += 1
                            
                # from bottom right
                if i + 1 < len(input_mat) and j + 1 < len(input_mat[i]) and input_mat[i+1][j+1] == "X":
                    if i - 2 >= 0 and j - 2 >= 0:
                        if input_mat[i-1][j-1] == "A" and input_mat[i-2][j-2] == "S":
                            res += 1
    return res

def solve2(input_mat: List[List[int]]) -> int:
    res = 0
    
    for i in range(1, len(input_mat) - 1):
        for j in range(1, len(input_mat[i]) - 1):
            if input_mat[i][j] == "A":
                is_x_shape = 2
                
                if input_mat[i-1][j-1] == "M" and input_mat[i+1][j+1] == "S":
                    is_x_shape -= 1
                    
                if input_mat[i-1][j+1] == "M" and input_mat[i+1][j-1] == "S":
                    is_x_shape -= 1
                    
                if input_mat[i+1][j-1] == "M" and input_mat[i-1][j+1] == "S":
                    is_x_shape -= 1
                
                if input_mat[i+1][j+1] == "M" and input_mat[i-1][j-1] == "S":
                    is_x_shape -= 1 
                
                if is_x_shape == 0:
                    res += 1
    return res

# Test the solution
# print(solve1(read_input("sample")))
# print(solve1(read_input("input")))

print(solve2(read_input("sample")))
print(solve2(read_input("input")))