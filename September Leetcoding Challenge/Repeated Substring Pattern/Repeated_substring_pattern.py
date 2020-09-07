class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        if not s:
            return False
        if(s in s[1:]+s[:-1]):
            return True
        else:
            return False