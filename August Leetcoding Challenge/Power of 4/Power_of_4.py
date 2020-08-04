class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        r=0
        while(num>=4):
            r= num%4
            if(r==0):
                num=num/4
            else:
                return False
        
        if(num==1):
            return True
        else:
            return False
        