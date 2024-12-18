
def lengthOfLongestSubstring(s: str) -> int:
    if len(s) < 2: return len(s)
    
    l, r = 0, 1
    max_len = 1
    seq_set = set()
    
    seq_set.add(s[l])
    
    while r < len(s):
        while s[r] in seq_set:
            seq_set.remove(s[l])
            l += 1
            
        seq_set.add(s[r])
        cur_len = r - l + 1
        max_len = max(max_len, cur_len)
        r += 1
        
    return max_len

print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))        
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring("zxyzxyz"))
print(lengthOfLongestSubstring("xxxx"))
print(lengthOfLongestSubstring("abba"))