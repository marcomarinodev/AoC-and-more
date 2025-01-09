
from typing import Optional
from tree_utils import TreeNode

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def get_arr(root: Optional[TreeNode]) -> list[int]:
            if not root:
                return [None]
            
            left_subtree = get_arr(root.left)
            right_subtree = get_arr(root.right)
            
            return [root.val] + left_subtree + right_subtree
        
        p_arr, q_arr = get_arr(p), get_arr(q)
        
        print(p_arr)
        print(q_arr)
        
        if len(p_arr) != len(q_arr):
            return False
        
        for i in range(len(p_arr)):
            if p_arr[i] != q_arr[i]:
                return False
            
        return True
    
    
sol = Solution()
root = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

print(sol.isSameTree(root, root2))
        
