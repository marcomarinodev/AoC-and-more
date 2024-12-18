
from typing import List

def read_levels(filename: str) -> List[List[int]]:
    levels_mat = []
    with open(filename) as file:
        for line in file:
            levels_mat.append([int(x) for x in line.split()])
    return levels_mat

def is_safe(levels: List[int]) -> bool:
    inc = {levels[i + 1] - levels[i] for i in range(len(levels) - 1)}
    return inc <= {1,2,3} or inc <= {-1,-2,-3}

def solve1(levels_mat: List[List[int]]) -> int:
    return sum([is_safe(level) for level in levels_mat])

def solve2(levels_mat: List[List[int]]) -> int:
    return sum(
        any(is_safe(level[:i] + level[i+1:]) for i in range(len(level)))
        for level in levels_mat
    )

print(solve1(read_levels("input")))
print(solve1(read_levels("sample")))

print(solve2(read_levels("input")))
print(solve2(read_levels("sample")))