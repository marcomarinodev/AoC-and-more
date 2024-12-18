import re

def read_string(filename: str) -> str:
    with open(filename) as file:
        return file.read().replace('\n', '')
    
def solve1(input_str: str) -> int:
    expressions = re.findall(r"mul\((\d+\,\d+)\)", input_str)
    
    return sum([int(op[0])*int(op[1]) for op in [exp.split(",") for exp in expressions]])

def solve2(input_str: str) -> int:
    raw_expressions = re.split(r"(do\(\)|don't\(\))", input_str)
    
    res = 0
    do = True
    for exp in raw_expressions:
        if exp == "don't()":
            do = False
            continue
        
        if exp == "do()":
            do = True
            continue
        
        if do:
            res += solve1(exp)
    return res

# print(solve1(read_string("input")))
# print(solve1(read_string("sample.txt")))

print(solve2(read_string("input")))
print(solve2(read_string("sample2.txt")))


