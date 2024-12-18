from typing import List, Union

def read_mat(filename: str) -> List[List[List[Union[str, bool]]]]:
    mat = []
    with open(filename) as file:
        for line in file:
            mat.append([[el, False] for el in line[:-1]])
    return mat

def place_and_count_antennas(input_mat: List[List[List[Union[str, bool]]]]) -> int:
    def place_antenna(res_mat, i, j, row, col, res):
        if not res_mat[row][col][1]:
            res_mat[row][col][1] = True
            res += 1
        if not res_mat[i][j][1]:
            res_mat[i][j][1] = True
            res += 1
        
        antenna_row = row + (row - i)
        antenna_col = col + (col - j) if j <= col else col - (j - col)
        
        while 0 <= antenna_row < len(res_mat) and 0 <= antenna_col < len(res_mat[0]):
            if not res_mat[antenna_row][antenna_col][1]:
                res_mat[antenna_row][antenna_col][1] = True
                res += 1
            
            antenna_row = antenna_row + (row - i)
            antenna_col = antenna_col + (col - j) if j <= col else antenna_col - (j - col)

        return res

    res = 0
    res_mat = input_mat

    # Top-down traversal
    for i in range(len(res_mat)):
        for j in range(len(res_mat[i])):
            pointed_char = res_mat[i][j][0]
            if pointed_char != ".":
                for row in range(i + 1, len(res_mat)):
                    for col in range(len(res_mat[row])):
                        cur_char = res_mat[row][col][0]
                        if cur_char == pointed_char:
                            res = place_antenna(res_mat, i, j, row, col, res)

    # Bottom-up traversal
    for i in range(len(res_mat) - 1, -1, -1):
        for j in range(len(res_mat[i])):
            pointed_char = res_mat[i][j][0]
            if pointed_char != ".":
                for row in range(i - 1, -1, -1):
                    for col in range(len(res_mat[row])):
                        cur_char = res_mat[row][col][0]
                        if cur_char == pointed_char:
                            res = place_antenna(res_mat, i, j, row, col, res)

    return res

print(place_and_count_antennas(read_mat("sample.txt")))
print(place_and_count_antennas(read_mat("input.txt")))