
from collections import defaultdict, deque

class Node:
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def get_adj_list(node: Node):
    adj_list = defaultdict(list[int])
    visited = set()
    to_visit = deque()
    
    to_visit.append(node)
    visited.add(node)
    
    while to_visit:
        cur_node = to_visit.popleft()
        
        for n in cur_node.neighbors:
            if n not in visited:
                adj_list[cur_node.val].append(n.val)
                adj_list[n.val].append(cur_node.val)
                to_visit.append(n)
                visited.add(n)
    return adj_list


    
    
    