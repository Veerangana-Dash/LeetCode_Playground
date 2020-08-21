class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        start=0
        end=len(A)-1
        result = []
        if(len(A)==1):
            return A
        
        for i in A:
            if(i%2 == 0):
                result.insert(start,i)
                start+=1
            else:
                result.insert(end,i)
                end-=1
            print(i)
        
        return result
            
            
        