
from typing import List
from collections import Counter

def read_list(filename: str) -> List[int]:
    file = open(filename, 'r')
    res = list(map(int, file.read().split()))
    file.close()
    return res

def get_halves(input_int: int) -> List[int]:
    input_str = str(input_int)
    split_idx = int(len(str(input_int)) / 2)
    return [int(input_str[:split_idx]), int(input_str[split_idx:])]

def blink(stones_dict):
    res_dict = Counter()
    
    for key in stones_dict.keys():
        if key == 0:    
            # if I have x zeros, they become x ones
            res_dict[1] += stones_dict[key] 
            continue
        
        if len(str(key)) % 2 == 0:
            halves = get_halves(key)
            res_dict[halves[0]] += stones_dict[key]
            res_dict[halves[1]] += stones_dict[key]
            continue
        
        res_dict[key * 2024] += stones_dict[key]
    return res_dict

res = read_list("input.txt")

stones_dict = Counter(res)

for i in range(75):
    stones_dict = blink(stones_dict)
    
print(sum(stones_dict.values()))

