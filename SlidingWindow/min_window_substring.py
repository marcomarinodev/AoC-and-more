
from collections import Counter, defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "":
            return ""
        
        t_count = Counter(t)
        window_count = defaultdict(int)
        l = r = 0
        res, res_len = [-1, -1], float("inf")
        have, required = 0, len(t_count)
        
        while r < len(s):
            window_count[s[r]] += 1
            
            if window_count[s[r]] == t_count[s[r]]:
                have += 1
            
            while have == required:
                if res_len > r - l + 1:
                    res_len = r - l + 1
                    res = [l, r]
                
                window_count[s[l]] -= 1
                if window_count[s[l]] < t_count[s[l]]:
                    have -= 1
                l += 1
                
            r += 1
         
        return s[res[0]:res[1] + 1] if res_len != float("inf") else ""
            
sol = Solution()

print(sol.minWindow("ADOBECODEBANC", "ABC")) # BANC
print(sol.minWindow("OUZODYXAZV", "XYZ")) # YXAZ
print(sol.minWindow("a", "a")) # a
print(sol.minWindow("a", "aa")) 