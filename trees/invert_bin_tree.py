
from typing import Optional
from tree_utils import TreeNode, print_tree

class Solution:
    
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root == None:
            return None

        tmp = root.left
        root.left = root.right
        root.right = tmp
        
        self.invertTree(root.left)
        self.invertTree(root.right)
        
        return root
    
sol = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3, TreeNode(6), TreeNode(7)))

print_tree(root)
print_tree(sol.invertTree(root))

# print(sol.invertTree(root))
