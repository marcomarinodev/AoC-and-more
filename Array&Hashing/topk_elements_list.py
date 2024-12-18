from typing import List
from collections import defaultdict
import heapq

# TIME: O(n * log k), SPACE: O(n)
def topk_frequent_minheap(nums: List[int], k: int) -> List[int]:
    dict_nums = defaultdict(int)
    min_heap = []
    
    for num in nums:
        dict_nums[num] += 1
        
    for num in dict_nums.keys():
        heapq.heappush(min_heap, (dict_nums[num], num))
        if len(min_heap) > k:
            heapq.heappop(min_heap)

    return [num for (_, num) in min_heap]

# TIME: O(n), SPACE: O(n)
def topk_frequent_bucket_sort(nums: List[int], k: int) -> List[int]:
    dict_nums = defaultdict(int)
    freq_keeper = [[] for i in range(len(nums) + 1)]
    
    for num in nums:
        dict_nums[num] += 1
    
    for num in dict_nums.keys():
        freq_keeper[dict_nums[num]].append(num)
        
    res = []
    for i in range(len(freq_keeper) - 1, -1, -1):
        for num in freq_keeper[i]:
            res.append(num)
            if len(res) == k:
                return res    

            
nums = [1,2,2,3,3,3]
nums_1 = [1,1,1,2,2,3]

