
from tree_utils import TreeNode
from typing import Optional

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        max_res = float("-inf")
        
        def dfs(root: Optional[TreeNode]):
            nonlocal max_res
            if root is None:
                return 0
            
            left_res = max(dfs(root.left), 0)
            right_res = max(dfs(root.right), 0)
            
            max_res = max(max_res, root.val + left_res + right_res)
            
            return root.val + max(left_res, right_res)

        dfs(root)
        
        return max_res
    
sol = Solution()
