class Solution:
    def titleToNumber(self, s: str) -> int:
        size = len(s)
        result = 0
        
        for i in range(size):
            result = result*26 + (ord(s[i]) - ord('A')) + 1
            print (result)
        return result
            
        