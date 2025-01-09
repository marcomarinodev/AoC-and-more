
from typing import Optional
from tree_utils import TreeNode, print_tree

class Solution:
    # Time: O(n), Space: O(n)
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        
        # it returns the height and it saves the maximum span
        def dfs(curr: TreeNode):
            if curr is None:
                return 0
            
            left_height = dfs(curr.left)
            right_height = dfs(curr.right)
            
            self.diameter = max(self.diameter, left_height + right_height)
            return 1 + max(left_height, right_height)
        
        dfs(root)
        
        return self.diameter

                