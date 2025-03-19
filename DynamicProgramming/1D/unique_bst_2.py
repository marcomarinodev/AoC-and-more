
from Trees.tree_utils import TreeNode

from typing import List, Optional

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        if n == 0:
            return []

        # (start, end) => subtrees as list
        cache = {}

        def build_subtrees(start, end) -> list:
            if start > end:
                return [None]
            
            if (start, end) in cache:
                return cache[(start, end)]
            
            all_trees = []

            for i in range(start, end + 1):
                all_left_subtrees = build_subtrees(start, i - 1)
                all_right_subtrees = build_subtrees(i + 1, end)

                for left in all_left_subtrees:
                    for right in all_right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        all_trees.append(root)
                
                cache[(start, end)] = all_trees
            
            return all_trees
        
        return build_subtrees(1, n)