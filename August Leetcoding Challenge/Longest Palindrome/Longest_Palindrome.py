class Solution:
    def longestPalindrome(self, s: str) -> int:
        d=collections.Counter(s)
        odd,total = 0,0
        
        for i in d:
            if(d[i]%2!=0):
                odd +=1
            total += d[i]
        
        return min(total,total-odd+1)
        