class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        
        result =[0]*num_people
        
        i=0
        start =1
        while(candies):
            if(candies-start>=0):
                result[i%num_people] +=start
                candies = candies - start
            else:
                result[i%num_people] +=candies
                candies=0
                
                
            
            start+=1
            i+=1
            
        
        return result
            
        