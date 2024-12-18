
from typing import List
from collections import deque

def read_disk_map(filename: str) -> List[int]:
    res = []
    with open(filename) as file:
        for line in file:
            for num in line:
                res.append(int(num))
    return res

def expand(disk_map: List[int]) -> List[int]:
    res = []
    
    file_id = 0
    for i in range(len(disk_map)):
        if i % 2 == 0:
            res += [file_id] * disk_map[i]
            file_id += 1
        else:
            res += [-1] * disk_map[i]
    return res

def compact(expanded_disk_map: List[int]) -> List[int]:
    
    free_space_queue = deque([])
    
    for i in range(len(expanded_disk_map)):
        if expanded_disk_map[i] == -1:
            free_space_queue.append(i)
    
    for i in range(len(expanded_disk_map) - 1, -1, -1):
        if free_space_queue and expanded_disk_map[i] != -1:
            if free_space_queue[0] < i: 
                first_free_space_pos = free_space_queue.popleft()
                expanded_disk_map[first_free_space_pos] = expanded_disk_map[i]
                expanded_disk_map[i] = -1
        
    return expanded_disk_map

def find_block_space(requested_block_size: int, free_space_map: deque) -> List[int]:
    l = 0
    cur_block = []

    while l < len(free_space_map):
        if free_space_map[l] >= 0:
            if not cur_block or free_space_map[l] - cur_block[-1] == 1:
                cur_block.append(free_space_map[l])
                if len(cur_block) == requested_block_size:
                    return cur_block
            else:
                cur_block = [free_space_map[l]]
        else:
            cur_block = []
        l += 1  
    
    return [] 

def compact_with_blocks(expanded_disk_map: List[int]) -> List[int]:
    free_space_queue = deque([])
    
    for i in range(len(expanded_disk_map)):
        if expanded_disk_map[i] == -1:
            free_space_queue.append(i)
            
    cur_block_indices = [len(expanded_disk_map) - 1]
    cur_block = expanded_disk_map[-1]
    progress_count = 1
    for i in range(len(expanded_disk_map) - 2, -1, -1):
        print(f"{progress_count}/{len(expanded_disk_map)}")
        progress_count += 1
        if expanded_disk_map[i] != cur_block:
            block_size = len(cur_block_indices)
            free_space_positions = find_block_space(block_size, free_space_queue)
            
            for free_pos in free_space_positions:
                if free_pos < cur_block_indices[-1]:
                    expanded_disk_map[free_pos] = cur_block
                    index_to_free = cur_block_indices.pop()
                    expanded_disk_map[index_to_free] = -1
                    free_space_queue.remove(free_pos)
                
            cur_block_indices = []
            cur_block = expanded_disk_map[i]
        
        if cur_block != -1:
            cur_block_indices.append(i)
    
    return expanded_disk_map

def compute_checksum(compacted_disk_map: List[int]) -> int:
    res = 0
    
    for i in range(len(compacted_disk_map)):
        if compacted_disk_map[i] != -1:
            res += i * compacted_disk_map[i]
    return res

# print(compute_checksum(compact(expand(read_disk_map("sample2.txt")))))
# print(compute_checksum(compact(expand(read_disk_map("input.txt")))))

print(compute_checksum(compact_with_blocks(expand(read_disk_map("sample2.txt")))))
print(compute_checksum(compact_with_blocks(expand(read_disk_map("input.txt")))))