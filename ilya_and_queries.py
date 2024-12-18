from typing import List

def read_input():
    
    input_str = input()
    input_pairs = []
    
    n = int(input())
    
    for _ in range(n):
        input_pairs.append([int(x) - 1 for x in input().split()])
    
    return (input_str, input_pairs)

def solve(input_str: str, pairs: List[List[int]]) -> int:
    prefix_sum = []
    cur_sum = 0
    res = 0
    
    for i in range(len(input_str)):
        if i < len(input_str) - 1 and input_str[i] == input_str[i+1]:
            cur_sum += 1
        prefix_sum.append(cur_sum)
        
    for pair in pairs:
        to_substract = 0
        if pair[0] - 1 >= 0:
            to_substract = prefix_sum[pair[0] - 1]
            
        print(prefix_sum[pair[1] - 1] - to_substract)

    return res

input_str, input_pairs = read_input()


solve(input_str, input_pairs)
            
    
# #..###
# 5
# 1 3
# 5 6
# 1 5
# 3 6
# 3 4

# ......
# 4
# 3 4
# 2 3
# 1 6
# 2 6