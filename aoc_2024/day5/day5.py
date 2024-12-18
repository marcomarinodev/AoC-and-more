from typing import List
from collections import defaultdict

def read_input_pairs(filename: str) -> List[List[int]]:
    input_pairs = []
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if not line:
                break
            input_pairs.append(list(map(int, line.split("|"))))
    return input_pairs

def read_input_lists(filename: str) -> List[List[int]]:
    input_lists = []
    
    start_reading = False
    with open(filename) as file:
        for line in file:
            line = line.strip()
            if not line:
                start_reading = True
                continue
            
            if start_reading:
                input_lists.append(list(map(int, line.split(","))))
    return input_lists

def solve(input_pairs: List[List[int]], input_lists: List[List[int]]) -> List[int]:
    
    page_dict = defaultdict(list)
    res = [0, 0]
    
    for pair in input_pairs:
        page_dict[pair[0]].append(pair[1])
        
    for in_list in input_lists:
        is_correct = True
        
        for i in range(len(in_list)):
            for page_j in in_list[i+1:]:
                if page_j not in page_dict[in_list[i]]:
                    is_correct = False
        
        if is_correct:
            res[0] += in_list[int(len(in_list) / 2)]
            continue
            
        for i in range(len(in_list)):
            left_count = right_count = 0
            for page_j in in_list[:i] + in_list[i+1:]:
                if page_j not in page_dict[in_list[i]]:
                    # it means page_j is smaller than in_list[i]
                    # left count increases
                    left_count += 1
                else:
                    right_count += 1
            if left_count == right_count:
                # the element in the middle has the same number of left 
                # and right elements assuming the list is odd
                res[1] += in_list[i]
    
    return res
    
# print(solve1(read_input_pairs("input"), read_input_lists("input")))
print(solve(read_input_pairs("sample"), read_input_lists("sample"))[0])
print(solve(read_input_pairs("sample"), read_input_lists("sample"))[1])

print(solve(read_input_pairs("input"), read_input_lists("input"))[0])
print(solve(read_input_pairs("input"), read_input_lists("input"))[1])