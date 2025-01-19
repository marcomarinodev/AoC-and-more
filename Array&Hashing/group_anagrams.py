
from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        
        for st in strs:
            chars_count = [0] * 26
            for c in st:
                chars_count[ord(c) - ord('a')] += 1
            
            anagrams[tuple(chars_count)].append(st)
            
        return [word_list for _, word_list in anagrams.items()]
    
sol = Solution()
in1 = ["act","pots","tops","cat","stop","hat"]

print(sol.groupAnagrams(in1))