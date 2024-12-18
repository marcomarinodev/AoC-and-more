import numpy as np
import heapq
from typing import List, Tuple, Dict, Set

def read_bytes_coordinates(filename: str) -> list[list[int]]:
    res = []
    with open(filename) as file:
        for line in file:
            res.append(list(map(int, line.split(","))))
    return res

def mat_after_n(n: int, size: int, coordinates: list[list[int]]) -> list[list[str]]:
    mat = [["."] * size for _ in range(size)]
    for i in range(n):
        x, y = coordinates[i]
        mat[y][x] = "#"
    return mat

def create_node(position: Tuple[int, int], g: float = float('inf'),
                h: float = 0.0, parent: Dict = None) -> Dict:
    return {
        'position': position,
        'g': g,
        'h': h,
        'f': g + h,
        'parent': parent
    }

def compute_manhattan(point1: tuple[int, int], point2: tuple[int, int]) -> int:
    return abs(point1[1] - point2[1]) + abs(point1[0] - point2[0])

def reconstruct_path(goal_node: Dict) -> List[Tuple[int, int]]:
    path = []
    current = goal_node
    while current is not None:
        path.append(current['position'])
        current = current['parent']
    return path[::-1]

def a_star(input_mat: list[list[str]]) -> List[Tuple[int, int]]:
    start, target = (0, 0), (len(input_mat) - 1, len(input_mat) - 1)
    start_node = create_node(position=start, g=0, h=compute_manhattan(start, target))
    to_visit = [(start_node['f'], start)]
    nodes_dict = {start: start_node}
    visited = set()

    while to_visit:
        _, cur_pos = heapq.heappop(to_visit)
        if cur_pos in visited:
            continue
        visited.add(cur_pos)
        
        cur_node = nodes_dict[cur_pos]
        if cur_pos == target:
            return reconstruct_path(cur_node)
        
        dirs = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        for dir in dirs:
            move_row, move_col = cur_pos[0] + dir[0], cur_pos[1] + dir[1]
            if 0 <= move_row < len(input_mat) and 0 <= move_col < len(input_mat):
                if input_mat[move_row][move_col] == "#":
                    continue
                neighbor_pos = (move_row, move_col)
                tentative_g = cur_node['g'] + 1  # Step cost is 1 for Manhattan grid
                
                if neighbor_pos not in nodes_dict or tentative_g < nodes_dict[neighbor_pos]['g']:
                    neighbor = create_node(
                        position=neighbor_pos,
                        g=tentative_g,
                        h=compute_manhattan(neighbor_pos, target),
                        parent=cur_node
                    )
                    nodes_dict[neighbor_pos] = neighbor
                    heapq.heappush(to_visit, (neighbor['f'], neighbor_pos))
                    
    return []  # Return empty path if no solution found

def check_first_no_exit_pair(size: int, bytes_coordinates: list[list[int]]) -> list[int]:
    # Create a mutable 2D matrix (list of lists of characters)
    input_mat = [["." for _ in range(size)] for _ in range(size)]
    
    backtrace = None
    for point in bytes_coordinates:
        # you can avoid points that are not in the optimal path
        # as they won't stop the path
        
        # Mark the point as an obstacle
        input_mat[point[1]][point[0]] = "#"
        backtrace = a_star(input_mat)
        
        if len(backtrace) == 0:
            print(f"No path found after blocking point: {point}")
            break
        
    return point

# Example usage
filename = "input.txt"
bytes_coordinates = read_bytes_coordinates(filename)

print(check_first_no_exit_pair(71, bytes_coordinates))

# input_mat = mat_after_n(1024, 71, bytes_coordinates)

# path = a_star(input_mat)
# print(input_mat)
# print("Path length:", len(path) - 1)
# print("Path:", path)