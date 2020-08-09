class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        rows=len(grid)
        cols=len(grid[0])
        
        #empty grid
        if rows==0:
            return -1
       
        #dict for rotten (BFS)
        rotten = {(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 2}
        
        #dict for fresh (BFS)
        fresh = {(i,j) for i in range(rows) for j in range(cols) if grid[i][j] == 1}
        
        #initialize timer
        count =0
        
        #iterate till fresh oranges are left
        while fresh:

            #fresh is not rotten, some fresh is left
            if not rotten:
                return -1
            
            #add adjacent fresh oranges to rotten
            rotten ={(i+di, j+dj) for i,j in rotten for di,dj in [(0,1),(1,0),(0,-1),(-1,0)] if (i+di,j+dj) in fresh}
            #remove from fresh
            fresh = fresh - rotten

            #update timer
            count +=1
        
        return count
        