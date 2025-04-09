
from typing import Optional, List
from tree_utils import printTree, TreeNode

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        
        max_el = float("-inf")
        max_el_i = -1
        
        for i in range(len(nums)):
            if nums[i] > max_el:
                max_el = nums[i]
                max_el_i = i
        
        cur_node = TreeNode(max_el)
        
        cur_node.left = self.constructMaximumBinaryTree(nums[:max_el_i])
        cur_node.right = self.constructMaximumBinaryTree(nums[max_el_i + 1:])
        
        return cur_node
    
sol = Solution()
printTree(sol.constructMaximumBinaryTree([3,2,1,6,0,5]))