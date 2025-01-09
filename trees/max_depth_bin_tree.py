from typing import Optional
from tree_utils import TreeNode, print_tree

class Solution:
    def maxDepth(self, root:Optional[TreeNode]) -> int:
        to_visit: list[tuple[TreeNode, int]] = []
        max_depth = 0
        
        if root is not None:
            to_visit.append((root, 1))
        
        while to_visit:
            node, depth = to_visit.pop()
            max_depth = max(max_depth, depth)
            
            if node.right is not None:
                to_visit.append((node.right, depth + 1))
            
            if node.left is not None:
                to_visit.append((node.left, depth + 1))
            
        return max_depth
                
sol = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4)))
root2 = TreeNode(1, TreeNode(2, TreeNode(5, TreeNode(7)), TreeNode(6)),
    TreeNode(3, TreeNode(4)))

print(sol.maxDepth(root2))