
def strStr(haystack: str, needle: str) -> int:

    if len(needle) > len(haystack):
        return -1
    
    for i in range(len(haystack)):
        if haystack[i:len(needle) + i] == needle:
            return i
        
    return -1
    
print(strStr("sadbutsad", "sad"))
print(strStr("leetcode", "leeto"))
