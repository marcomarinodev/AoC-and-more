
from typing import Optional, List
from tree_utils import TreeNode

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        levels = self.get_levels(root)
        
        for l in levels:
            res.append(l[-1])
            
        return res
    
    def get_levels(self, root: Optional[TreeNode]) -> List[List[int]]:
        levels = []
        
        if not root:
            return levels
        
        to_visit: List[tuple[Optional[TreeNode], int]] = [(root, 0)]
        
        while to_visit:
            node, depth = to_visit.pop()
            
            if len(levels) <= depth:
                levels.append([node.val])
            else:
                levels[depth].append(node.val)
                
            if node.right != None:
                to_visit.append((node.right, depth + 1))
                
            if node.left != None:
                to_visit.append((node.left, depth + 1))
        
        return levels
    
sol = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, 
            TreeNode(2, TreeNode(4, TreeNode(17, TreeNode(18))), TreeNode(5, None, TreeNode(9))), 
            TreeNode(3, TreeNode(6))
    )
root3 = None
print(sol.rightSideView(root))
print(sol.rightSideView(root2))
print(sol.rightSideView(root3))