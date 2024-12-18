from typing import List
from collections import defaultdict

def read_input_pairs(input_filename: str) -> tuple[List[int], List[int]]:
    l1 = []
    l2 = []
    with open(input_filename) as input_file:
        for line in input_file:
            values = line.split()
            l1.append(int(values[0]))
            l2.append(int(values[1]))
    return (l1, l2)

def solve(lists: tuple[List[int], List[int]]) -> int:
    lists[0].sort()
    lists[1].sort()
    res = 0
    
    i = 0
    while i < len(lists[0]) and i < len(lists[1]):
        res += abs(lists[0][i] - lists[1][i])
        i += 1

    return res

def solve2(lists: tuple[List[int], List[int]]) -> int:
    l2_dict = defaultdict(int)
    res = 0
    
    for el in lists[1]:
        l2_dict[el] += 1
        
    for el in lists[0]:
        res += el * l2_dict[el]
        
    return res
        

# print(solve(read_input_pairs("input")))
# print(solve(read_input_pairs("input2")))
print(solve2(read_input_pairs("input")))
# print(solve2(read_input_pairs("input2")))
