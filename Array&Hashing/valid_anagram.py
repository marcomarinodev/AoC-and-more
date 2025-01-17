
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = defaultdict(int)
        
        if len(s) != len(t):
            return False
        
        for i in range(len(s)):
            s_dict[s[i]] += 1
            
        for i in range(len(t)):
            if t[i] not in s_dict:
                return False
            
            s_dict[t[i]] -= 1
            
        for k, v in s_dict.items():
            if v > 0:
                return False
        
        return True
    
sol = Solution()
s, t = "racecar", "carrace"
print(sol.isAnagram(s, t))

s, t = "jar", "jam"
print(sol.isAnagram(s, t))