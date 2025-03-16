

def validAbbreviation(word: str, abbr: str):
    i = j = 0
    cur_len = 0

    while i < len(abbr) and j < len(word):
        if abbr[i].isdigit():
            if int(abbr[i]) == 0 and cur_len == 0:
                return False
            cur_len = cur_len * 10 + int(abbr[i])
        else:
            j += cur_len
            cur_len = 0
            
            if j >= len(word) or abbr[i] != word[j]:
                return False
        
            j += 1
        i += 1
    
    j += cur_len
    
    return i == len(abbr) and j == len(word)

print(validAbbreviation("internationalization", "i12iz4n"))