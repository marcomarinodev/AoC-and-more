
from typing import Optional
from tree_utils import TreeNode

class Solution:
    
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True
        if not root: return False
        
        to_visit: list[TreeNode] = []
        curr = root
        res = False
        
        to_visit.append(root)
        
        while to_visit and not res:
            
            curr = to_visit.pop()
            
            if curr is None:
                continue
            
            res = self.isSubtreeHelper(curr, subRoot)
            
            if curr.right is not None:
                to_visit.append(curr.right)
            
            if curr.left is not None:
                to_visit.append(curr.left)
            
        return res
    
    def isSubtreeHelper(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        if root == None and subRoot == None:
            return True
        
        if root and subRoot and root.val == subRoot.val:
            check_left = self.isSubtreeHelper(root.left, subRoot.left)
            check_right = self.isSubtreeHelper(root.right, subRoot.right)
            
            return check_left and check_right
        
        return False
        
    
sol = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4, TreeNode(6)), TreeNode(5)), TreeNode(3))
root1 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3))
subRoot = TreeNode(2, TreeNode(4), TreeNode(5))

print(sol.isSubtree(root, subRoot))
print(sol.isSubtree(root1, subRoot))