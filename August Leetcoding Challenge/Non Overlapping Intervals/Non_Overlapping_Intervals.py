class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        count=0
        print(intervals)
        if(len(intervals)==0):
            return 0
        
        prev=intervals[0]
        
        for i in intervals[1:]:
            if(i[0]<prev[1] or i[0]==prev[0]):
                count+=1 
                
            if not i[0] < prev[1] < i[1]:
                prev=i
            
        return count

