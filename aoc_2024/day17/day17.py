# ip moves by 2 at every non jump instruction

# combo operands:
# 0,1,2,3 -> 0,1,2,3
# 4 -> A, 5 -> B, 6 -> C

# opcodes:
# 0 -> A / 2^combo_operand truncated to integer => A
# 1 -> B XOR 1 => B
# 2 -> combo_operand % 8 => B
# 3 -> nothing if A = 0, else ip to 3 and ip not increased by 2
# 4 -> B XOR C
# 5 -> combo_operand % 8 => output (separated by comma)
# 6 -> A / 2^combo_operand truncated to integer => B
# 7 -> A / 2^combo_operand truncated to integer => C

"""
Program: 2,4,1,3,7,5,4,2,0,3,1,5,5,5,3,0

GOAL: find the lowest A such that the output = program
CONSTRAINT: Input such that A is always 0 at the end

saying a // 2^3 it's the same as taking a in bits and shifting 
it to the right 3 times, so to reverse it we have to add 3 bits
back, so we have 2^3 combinations to test
"""

import math
from collections import defaultdict

def read_registers(filename: str) -> defaultdict:
    registers = defaultdict(int)
    with open(filename) as file:
        for line in file:
            if line.startswith("Register"):
                registers[line.split()[1][:-1]] = int(line.split()[2])
    return registers

def read_program(filename: str) -> list[int]:
    res = []
    with open(filename) as file:
        for line in file:
            if line.startswith("Program"):
                res = list(map(int, line.split()[1].split(",")))
    return res

filename = "sample.txt"

def get_operand_value(registers: defaultdict, operand: int) -> int:
    match operand:
        case 4: return registers["A"]
        case 5: return registers["B"]
        case 6: return registers["C"]
        case 7: return None
        case _:
            return operand

def run(registers: defaultdict, program: list[int]) -> list[int]:
    ip = 0
    out = []
    
    while ip < len(program):
        opcode = program[ip]
        literal_operand = program[ip + 1]
        combo_operand = get_operand_value(registers, literal_operand)
        if opcode == 0:
            registers["A"] = math.trunc(registers["A"] / pow(2, combo_operand))
            ip += 2
        elif opcode == 1:
            registers["B"] = registers["B"] ^ literal_operand
            ip += 2
        elif opcode == 2:
            registers["B"] = combo_operand % 8
            ip += 2
        elif opcode == 3:
            if registers["A"] != 0:
                ip = literal_operand
            else:
                ip += 2
        elif opcode == 4:
            registers["B"] = registers["B"] ^ registers["C"]
            ip += 2
        elif opcode == 5:
            out.append(combo_operand % 8)
            ip += 2
        elif opcode == 6:
            registers["B"] = math.trunc(registers["A"] / pow(2, combo_operand))
            ip += 2
        elif opcode == 7:
            registers["C"] = math.trunc(registers["A"] / pow(2, combo_operand))
            ip += 2
            
    return out

def reverse_engineer(program: list[int]) -> int:
    valid_vals_for_a = {0}
    
    for i in range(len(program) - 1, -1, -1):
        instr = program[i]
        next_vals_for_a = set()
        
        for a_val in valid_vals_for_a:
             # equivalent to left shift by 3, so now we can add any three bits
            a_shifted = a_val * 8
            
            for candidate_a in range(a_shifted, a_shifted + 8): # try all 8 possible values            
                registers = defaultdict(int)
                registers["A"] = candidate_a
                out = run(registers, program)
                # if last program int == first generated output
                # then proceed with this candidate
                if out and out[0] == instr:
                    good_out = out
                    next_vals_for_a.add(candidate_a)
                    
        print(f"out={good_out}")
        valid_vals_for_a = next_vals_for_a
        
    return min(valid_vals_for_a)

filename = "input.txt"
registers = read_registers(filename)
program = read_program(filename)

print(reverse_engineer(program))