
from typing import Optional
from tree_utils import TreeNode

class Solution:
    
    def goodNodes(self, root: TreeNode) -> int:
    
        def helper(curr: TreeNode, max_val):
            if curr == None:
                return 0
            
            res = 1 if curr.val >= max_val else 0
            new_max_val = max(max_val, curr.val)
            res += helper(curr.left, new_max_val)
            res += helper(curr.right, new_max_val)
            
            return res
        
        return helper(root, root.val)
    
sol = Solution()
root = TreeNode(2, TreeNode(1, TreeNode(3)), TreeNode(1, TreeNode(1), TreeNode(5)))
root2 = TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)), TreeNode(-1))
root3 = None
root4 = TreeNode(3, TreeNode(3, TreeNode(4), TreeNode(2)))

print(sol.goodNodes(root))
print(sol.goodNodes(root2))
print(sol.goodNodes(root3))
print(sol.goodNodes(root4))