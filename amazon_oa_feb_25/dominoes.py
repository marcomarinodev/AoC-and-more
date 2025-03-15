
"""
Amazon Games has launched a new game involving dominoes. The game consists of n dominoes, each with a specific size denoted by the array domino. The "order" of the dominoes is defined as the length of the longest strictly increasing subsequence (LIS) of their sizes.

There is also an array remove that contains integers from 0 to n-1. In each move, the player can remove the domino specified by the remove array. The goal is to determine the maximum number of moves that can be made such that, after these removals, the order of the remaining dominoes is at least equal to a given integer min_order.

Example:
n = 6

domino = [1, 4, 4, 2, 5, 3]

remove = [2, 1, 4, 0, 5, 3]

min_order = 3

In this example, the player can remove dominoes in the order specified by remove. After each removal, the length of the LIS of the remaining dominoes should be at least min_order. The task is to find out the maximum number of such removals possible.

Ans = 3

Hints:* Longest Increasing Subsequcne , Binary Search*
"""

from typing import List

class Solution:
    
    def bin_search(self, t: int, arr: list[int]) -> int:
        l, r = 0, len(arr) - 1
        
        while l != r:
            mid = l + (r - l) // 2
            if t > arr[mid]:
                l = mid + 1
            else:
                r = mid
        
        return l
        
    def len_of_lis(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        
        increasing_subseq = [nums[0]]
        
        for n in nums:
            if n > increasing_subseq[-1]:
                increasing_subseq.append(n)
                continue
            
            index_to_replace = self.bin_search(n, increasing_subseq)
            
            increasing_subseq[index_to_replace] = n
        
        return len(increasing_subseq)
    
    def get_max_moves(self, domino: list[int], remove: list[int], min_order: int) -> int:
        """
        bin search over the answer. If len(remove) == 6, then we start checking len of lis
        with all the moves [0:3]. If len of lis is < min_order, we search the answer on the left
        because we're removing elements with the increasing of the number of the moves...
        Otherwise we seek for the maximum number on the right side...
        
        This will use bin search O(log n). checking the len of list costs O(n * log n).
        Time Complexity: O(n * log n * log n)
        """
        
        # to access in constant time to the array without the elements pointed in the remove array
        # we build a dictionary
        
        # e.g, 3 removed at iteration 2
        removed_at = {remove[i]: i for i in range(len(domino))}
        
        def get_len_of_lis_after_moves(moves: int) -> int:
            remaining_dominoes = [domino[i] for i in range(len(domino)) if removed_at >= moves]
            return self.len_of_lis(remaining_dominoes)
        
        if get_len_of_lis_after_moves(0) < min_order:
            return -1
        
        l, r = 0 , len(remove)
        
        while r - l > 1:
            mid = l + (r - l) // 2
            
            if self.len_of_lis(mid) >= min_order:
                l = mid
            else:
                r = mid
        
        return l