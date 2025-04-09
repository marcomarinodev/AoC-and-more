
from typing import Optional
from collections import deque
from pprint import pprint

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
        

            
def printTree(root: Optional[TreeNode]):
    def get_height(node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        
        return 1 + max(get_height(node.left), get_height(node.right))
    
    def rec_print_tree(node: Optional[TreeNode], l, r, level):
        if node is None:
            return
        
        mid = l + (r - l) // 2
        
        res[level][mid] = str(node.val)
        
        rec_print_tree(node.left, l, mid, level + 1)
        rec_print_tree(node.right, mid, r, level + 1)
        
    height = get_height(root)
    ncols = 2**(height) - 1
    res = [[""] * ncols for _ in range(height)]
    
    rec_print_tree(root, 0, ncols, 0)
    
    pprint(res)
