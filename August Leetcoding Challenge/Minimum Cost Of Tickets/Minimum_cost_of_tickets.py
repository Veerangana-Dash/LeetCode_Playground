class Solution(object):
    def mincostTickets(self, days, costs):
        """
        :type days: List[int]
        :type costs: List[int]
        :rtype: int
        """
        last_day = days[-1]
        dp = [0]*(last_day +1)
        days = set(days)
        for d in range(1,last_day +1):
            if d in days:
                dp[d] = min(costs[2] + dp[max(d-30,0)], costs[1] + dp[max(d-7,0)], costs[0] + dp[d-1])
                
            else:
                dp[d] = dp[d-1]
        
        return dp[-1]
        