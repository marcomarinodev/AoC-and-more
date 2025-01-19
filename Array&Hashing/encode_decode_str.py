
from typing import List

class Solution:
    
    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""  # Return an empty string for an empty input list
        
        encoded_res = ""
        for st in strs:
            # Use the length of the string as a fixed-length prefix
            encoded_res += f"{len(st):04}"  # Fixed 4-digit length encoding
            encoded_res += st
        
        return encoded_res
    
    def decode(self, s: str) -> List[str]:
        if not s:
            return []  # Return an empty list for an empty input
        
        decoded_res = []
        i = 0
        while i < len(s):
            # Extract the fixed 4-digit length prefix
            length = int(s[i:i + 4])
            i += 4
            
            # Extract the string of the given length
            decoded_res.append(s[i:i + length])
            i += length
        
        return decoded_res
    
sol = Solution()
in1 = ["neet","code","love","you"]
in2 = [""]

print(sol.decode(sol.encode(in1)))
print(sol.decode(sol.encode(in2)))