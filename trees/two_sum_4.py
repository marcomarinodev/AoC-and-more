
from tree_utils import TreeNode
from typing import Optional
from collections import deque

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        diffs = {}
        to_visit = deque()
        
        to_visit.append(root)
        
        while to_visit:
            node = to_visit.popleft()
            
            if k - node.val in diffs:
                return True
            
            diffs[node.val] = k - node.val
            
            if node.left is not None:
                to_visit.append(node.left)
            
            if node.right is not None:
                to_visit.append(node.right)
        
        return False
            
            