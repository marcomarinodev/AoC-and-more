from typing import List
from collections import defaultdict

def read_input() -> List[int]:
    n = int(input())
    inputs = [int(x) for x in input().split()]
    
    return inputs
        
def solve(towers: List[int]) -> List[int]:
    towers_dict = defaultdict(lambda: 0)
    highest_tower = 0

    for t in towers:
        towers_dict[t] += 1
        highest_tower = max(highest_tower, towers_dict[t])
        
    return [highest_tower, len(towers_dict)]
            
output = solve(read_input())

print(output[0])
print(output[1])

