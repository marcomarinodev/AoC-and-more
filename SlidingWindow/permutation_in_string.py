
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1): 
            return False
        
        window_len = len(s1)
        l, r = 0, window_len - 1
        
        s1_chars_count, s2_chars_count = {}, {}
        
        for r in range(window_len):
            s2_chars_count[s2[r]] = s2_chars_count.get(s2[r], 0) + 1
            s1_chars_count[s1[r]] = s1_chars_count.get(s1[r], 0) + 1
            
        if s1_chars_count == s2_chars_count:
            return True
        
        r += 1 
        
        while r < len(s2):
            s2_chars_count[s2[l]] -= 1
            if s2_chars_count[s2[l]] == 0:
                del s2_chars_count[s2[l]]  # Remove key if count reaches 0
            
            s2_chars_count[s2[r]] = s2_chars_count.get(s2[r], 0) + 1
            
            if s1_chars_count == s2_chars_count:
                return True
            
            l += 1
            r += 1
            
        return False

sol = Solution()

print(sol.checkInclusion("ab", "eidbaooo"))
print(sol.checkInclusion("ab", "eidboaoo"))