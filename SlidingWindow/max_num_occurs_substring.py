
from collections import defaultdict

class Solution:
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        substr_count = defaultdict(int)
        char_freq = defaultdict(int)
        
        l = 0
        for r in range(len(s)):
            char_freq[s[r]] += 1
            
            if r - l + 1 > minSize:
                char_freq[s[l]] -= 1
                if char_freq[s[l]] == 0:
                    del char_freq[s[l]]
                l += 1
            
            if r - l + 1 == minSize:
                if len(char_freq) <= maxLetters:
                    substr = s[l:r+1]
                    substr_count[substr] += 1

        return max(substr_count.values(), default=0)
    
sol = Solution()
print(sol.maxFreq("aababcaab", 2, 3, 4)) # 2
print(sol.maxFreq("aaaa", 1, 3, 3)) # 2