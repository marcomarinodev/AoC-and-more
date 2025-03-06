from typing import List

from tree_utils import TreeNode

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents_map = {}
        
        def get_parents_map(root: TreeNode, parent: TreeNode):
            if root is None:
                return
            
            parents_map[root.val] = parent
            
            get_parents_map(root.left, root)
            get_parents_map(root.right, root)
            
        get_parents_map(root, None)
        
        visited = set()
        queue = [(target, 0)]
        res = []
        
        visited.add(target.val)
        
        while queue:
            to_visit_node, dist = queue.pop(0)
            
            if dist < k:
                if to_visit_node.left is not None and to_visit_node.left not in visited:
                    queue.append((to_visit_node.left, dist + 1))
                
                if to_visit_node.right is not None and to_visit_node.right not in visited:
                    queue.append((to_visit_node.right, dist + 1))
                
                if parents_map[to_visit_node.val] is not None and parents_map[to_visit_node.val] not in visited:
                    queue.append((parents_map[to_visit_node.val], dist + 1))
            
            if dist == k:
                res.append(to_visit_node.val)
                
            visited.add(to_visit_node)
        
        return res
    
sol = Solution()
target_node = TreeNode(5, TreeNode(6), TreeNode(2, TreeNode(7), TreeNode(4)) )
root = TreeNode(3,
    target_node,
    TreeNode(1, TreeNode(0), TreeNode(8))
)

print(sol.distanceK(root, target_node, 2))
