class Solution(object):
    def bSearch(self,prev,intervals,i,j):
        while i<j:
            mid = (i+j)//2
            if intervals[mid][0] ==prev:
                return mid
            elif intervals[mid][0] >prev:
                j=mid
            else:
                i=mid+1
        return i
        
    
    def findRightInterval(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[int]
        """
        ind = [b[0] for b in sorted(enumerate(intervals),key=lambda i:i[1])]
        intervals.sort(key=lambda a:a[0])
        res = [0]*len(intervals)
        for i in range(len(intervals)-1):
            r=self.bSearch(intervals[i][1],intervals,i+1,len(intervals))
            if( r<len(intervals)):
                res[ind[i]] = ind[r]
            else:
                res[ind[i]] = -1
        
        res[ind[-1]]=-1
        return res
            