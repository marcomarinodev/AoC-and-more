from typing import List, Set
from functools import cache

class Solution:
    def __init__(self, filename:str):
        self.filename = filename
        self.patterns = self.read_patterns()
        self.designs = self.read_designs()
        
    def read_patterns(self) -> Set[str]:
        res = set()
        with open(self.filename) as file:
            for line in file:
                res = line[:-1].split(", ")
                break
        return res

    def read_designs(self) -> List[str]:
        fin = open(self.filename)
        res = fin.read().split("\n")[2:]
        fin.close()
        return res
        
    @cache  
    def num_arrangements(self, design, start=0):
        if start >= len(design):    
            return 1
        result = 0
        for pattern in self.patterns:
            if design[start:start+len(pattern)] == pattern:
                result += self.num_arrangements(design, start + len(pattern))
        return result
    
    def solve1(self) -> int:
        return sum(self.num_arrangements(design) > 0 for design in self.designs)
                
    def solve2(self) -> int:
        return sum(self.num_arrangements(design) for design in self.designs)
                
sol = Solution("input.txt")
print(sol.solve2())