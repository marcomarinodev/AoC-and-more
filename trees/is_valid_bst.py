
from typing import Optional
from tree_utils import TreeNode

class Solution:
    def isValidBST(self, root:  Optional[TreeNode]) -> bool:
        
        def isValidBSTHelper(root: Optional[TreeNode], left, right) -> bool:
            if root == None:
                return True
            
            if not (left < root.val < right):
                return False
            
            check_left = isValidBSTHelper(root.left, left, root.val)
            check_right = isValidBSTHelper(root.right, root.val, right)
            
            return check_left and check_right
                        
        return isValidBSTHelper(root, float("-inf"), float("inf"))
            
        
    
sol = Solution()
root = TreeNode(2, TreeNode(1), TreeNode(3)) # true
root2 = TreeNode(1, TreeNode(2), TreeNode(3)) # false
root3 = None # true
root4 = TreeNode(5) # true
root5 = TreeNode(2, TreeNode(1, None, TreeNode(5)), TreeNode(9)) # false

print(sol.isValidBST(root))
print(sol.isValidBST(root2))
print(sol.isValidBST(root3))
print(sol.isValidBST(root4))
print(sol.isValidBST(root5))
        
        