# Write a function that joins two strings like this:
#      first the first letter of the first string, then the first letter of the second, second letter of the second, etc ...
#      The function should return a new string which is a combination of those given as parameters. Note: the input strings need not be the same length!
#      Example:
#      >> merge_strings ("dog", "cat")
#      dcoagt
#      >> merge_strings ("stop", "supermarket)
#      sstuoopermarket
#      If any string is longer, simply rewri

def merge_strings(first_w: str, second_w: str) -> str:
    l = r = 0
    res = ""
    
    while l < len(first_w) or r < len(second_w):
        
        if l < len(first_w):
            res += first_w[l]
            l += 1
        
        if r < len(second_w):
            res += second_w[r]
            r += 1
            
    return res
        
print(merge_strings("dog", "cat"))
print(merge_strings("stop", "supermarket"))
     
