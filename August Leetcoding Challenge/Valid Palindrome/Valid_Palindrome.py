class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i=0
        j=len(s)-1
        s=s.lower()
        a=''.join(e for e in s if e.isalnum())
        i=0
        j=len(a)-1
        while(i<j):
            if(a[i]==a[j]):
                    i+=1
                    j-=1
            else:
                    return False
            
        
        return True
        