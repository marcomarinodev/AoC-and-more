from collections import defaultdict

def findTheDifference(s: str, t: str) -> str:
    chars_dict = defaultdict(int)
    
    for c in s:
        chars_dict[c] += 1
        
    for c in t:
        if chars_dict[c] == 0:
            return c
        chars_dict[c] -= 1
    
    return ""

print(findTheDifference("abcd", "abcde"))
print(findTheDifference("", "y"))