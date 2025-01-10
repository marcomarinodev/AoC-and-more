
from typing import Optional, List
from tree_utils import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        if root == None:
            return []
        
        res = []
        to_visit = [(root, 0)]
        
        while to_visit:
            node, depth = to_visit.pop()
            
            if len(res) <= depth:
                res.append([node.val])
            else:
                res[depth].append(node.val)
                
            if node.right != None:
                to_visit.append((node.right, depth + 1))
                
            if node.left != None:
                to_visit.append((node.left, depth + 1))
                
        return res
    
sol = Solution()
root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
root2 = TreeNode(1)
root3 = None
root4 = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
print(sol.levelOrder(root))
print(sol.levelOrder(root2))
print(sol.levelOrder(root3))
print(sol.levelOrder(root4))