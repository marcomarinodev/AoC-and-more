
from tree_utils import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q:TreeNode) -> TreeNode:
        if root == None:
            return None
        
        if root.val == p.val or root.val == q.val:
            return root
        
        if root.val < max(p.val, q.val) and root.val > min(p.val, q.val):
            # anchestor, because it splits p and q
            # it is the minimum, otherwise it means that p and q
            # are both smaller or bigger than root
            return root
        
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)

        return self.lowestCommonAncestor(root.right, p, q)
    
sol = Solution()
q1 = TreeNode(4)
p = TreeNode(3, TreeNode(1, None, TreeNode(2)), q1)
q = TreeNode(8, TreeNode(7), TreeNode(9))
root = TreeNode(5, p, q)

print(sol.lowestCommonAncestor(root, p, q).val)
print(sol.lowestCommonAncestor(root, p, q1).val)