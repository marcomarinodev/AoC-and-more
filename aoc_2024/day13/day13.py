import re

def read_systems(filename: str) -> list[list[list[int]]]:
    systems = []
    with open(filename) as file:
        system = []
        for line in file:
            if line.startswith("Button A"):
                matches = re.findall(r"X\+(\d+)|Y\+(\d+)", line)
                a_x, a_y = (int(num) for pair in matches for num in pair if num)
                system.append([a_x, a_y])
                continue
            if line.startswith("Button B"):
                matches = re.findall(r"X\+(\d+)|Y\+(\d+)", line)
                b_x, b_y = (int(num) for pair in matches for num in pair if num)
                system.append([b_x, b_y])
                continue
            if line.startswith("Prize"):
                matches = re.findall(r"X\=(\d+)|Y\=(\d+)", line)
                p_x, p_y = (int(num) for pair in matches for num in pair if num)
                system.append([p_x, p_y])
        
                systems.append(system)
                system = []
    return systems

systems = read_systems("input.txt")

res = 0
offset = 10000000000000

# Cramer's method to solve 2x2 system of linear equations
# there's only one solution to the system and since it's the 
# only possible solution, the solution is the minimum one
for system in systems:
    (a_x, a_y), (b_x, b_y), (p_x, p_y) = system
    p_x, p_y = p_x + offset, p_y + offset
    det_mat = a_x * b_y - b_x * a_y
    a = int((p_x * b_y - b_x * p_y ) / det_mat)
    b = int((a_x * p_y - p_x * a_y) / det_mat)
    if p_x == a * a_x + b * b_x and p_y == a * a_y + b * b_y:
        res += a * 3 + b
        
print(res)