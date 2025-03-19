

class Solution:
    def numTrees(self, n: int) -> int:
        cache = {}

        def count_subtrees(start, end) -> int:
            if start > end:
                return 1  # An empty subtree is a valid subtree
            
            if (start, end) in cache:
                return cache[(start, end)]

            total_combos = 0
            for i in range(start, end + 1):
                left_combos = count_subtrees(start, i - 1)
                right_combos = count_subtrees(i + 1, end)

                total_combos += left_combos * right_combos  # Multiply left & right possibilities

            cache[(start, end)] = total_combos
            return total_combos

        return count_subtrees(1, n)
        