
class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        max_val = 1
        res = ""
        
        for i in range(len(number)):
            if number[i] == digit:
                subnum = number[:i] + number[i+1:]
                if int(subnum) >= max_val:
                    res = subnum
                    max_val = int(subnum)
        
        return res
    
sol = Solution()
print(sol.removeDigit("123", "3")) # 12
print(sol.removeDigit("1231", "1")) # 231
print(sol.removeDigit("551", "5")) # 51
print(sol.removeDigit("11", "1")) #
                