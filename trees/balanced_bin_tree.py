
from typing import Optional
from tree_utils import TreeNode

class Solution:
    
    # remember that when you want to bubble up something
    # from recursion, add it into the return object
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def helper(root) -> tuple[bool, int]:
            if root == None:
                return (True, 0)
            
            lb, lh = helper(root.left)
            rb, rh = helper(root.right)
            
            return (lb and rb and abs(lh - rh) <= 1, max(lh, rh) + 1)
    
        return helper(root)[0]