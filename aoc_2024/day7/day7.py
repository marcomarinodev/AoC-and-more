
from typing import List
from itertools import product

def read_input(filename: str) -> List[List[int]]:
    
    input_dict = []
    
    with open(filename) as file:
        lines = file.read().strip().split("\n")
        for line in lines:
            parts = line.split()
            value = int(parts[0][:-1])
            nums = list(map(int, parts[1:]))
            input_dict.append([value] + nums)
    return input_dict

def check(nums: List[int], combo) -> int:
    res = nums[0]
    
    for i in range(1, len(nums)):
        if combo[i-1] == "+":
            res += nums[i]
        elif combo[i-1] == "|":
            res = int(f"{res}{nums[i]}")
        else:
            res *= nums[i]
    return res   

def solve1(input_dict: List[List[int]]) -> int:
    res = 0
    
    for _input in input_dict:
        value = _input[0]
        nums = _input[1:]
        for combo in product("*+|", repeat=len(nums) - 1):
            if check(nums, combo) == value:
                res += value
                break
    return res

print(solve1(read_input("sample.txt")))
print(solve1(read_input("input.txt")))

