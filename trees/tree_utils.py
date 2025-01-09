
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right

def print_tree(root: Optional[TreeNode]):
        visited = []
        to_visit = deque()
        to_visit.appendleft(root)
        
        while to_visit:
            node = to_visit.popleft()
            visited.append(root.val)
            
            if node.left is not None:
                to_visit.append(root.left)
                
            if node.right is not None:
                to_visit.append(node.right)
        
        print(visited)