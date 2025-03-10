
class Solution:
        
    def get_max_count_in_window(self, count: list) -> int:
        max_count_char = ""
        max_count_in_window = 0
        for k, v in count.items():
            if v > max_count_in_window:
                max_count_char = k
                max_count_in_window = v
        return max_count_char
        
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        l = 0
        chars_count = {}
        
        for r in range(len(s)):
            
            if s[r] not in chars_count:
                chars_count[s[r]] = 1
            else:
                chars_count[s[r]] += 1
            
            max_count_char = self.get_max_count_in_window(chars_count)
            
            while (r - l + 1) - chars_count[max_count_char] > k:
                # this window is not valid if the characters to replace
                # are more than k
                chars_count[s[l]] -= 1
                l += 1
                max_count_char = self.get_max_count_in_window(chars_count)
                
            res = max(res, r - l + 1)
                
        return res
    
sol = Solution()

print(sol.characterReplacement("ABAB", 2))
print(sol.characterReplacement("AABABBA", 1))
