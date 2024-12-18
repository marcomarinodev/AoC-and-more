
def repeatedSubstringPattern1(s: str) -> bool:
    for i in range(len(s) // 2, 0, -1):
        if len(s) % i == 0:
            num_blocks = int(len(s) / i)
            sub_string = s[0:i]
            
            if s == sub_string * num_blocks:
                return True

    return False

def repeatedSubstringPattern2(s: str) -> bool:
    
    if not s:
        return False
    
    doubled_s = (s + s)[1:-1]
    return doubled_s.find(s) != -1

print(repeatedSubstringPattern2("abab"))
print(repeatedSubstringPattern2("aba"))
print(repeatedSubstringPattern2("abcabcabcabc"))