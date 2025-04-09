
from tree_utils import TreeNode

from typing import Optional

class Solution:
    first_pointer = None 
    second_pointer = None
    prev_pointer = TreeNode(float("-inf"))
    
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.in_order_traversal(root)
        
        tmp = self.first_pointer.val
        self.first_pointer.val = self.second_pointer.val
        self.second_pointer.val = tmp
        
    def in_order_traversal(self, root: Optional[TreeNode]):
        
        if root is None:
            return
        
        self.in_order_traversal(root.left)
        
        if self.first_pointer is None and root.val < self.prev_pointer.val:
            self.first_pointer = self.prev_pointer
            
        if self.first_pointer is not None and root.val < self.prev_pointer.val:
            self.second_pointer = root
            
        self.prev_pointer = root
        
        self.in_order_traversal(root.right)