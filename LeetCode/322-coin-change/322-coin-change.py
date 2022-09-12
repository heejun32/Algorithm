class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [0] + [-1] * (amount)
        
        for target in range(amount + 1):
            if dp[target] != -1:
                continue
            
            cost = float("inf")
            for coin in coins:
                if target - coin < 0 or dp[target - coin] == -1:
                    continue
                cost = min(cost, dp[target - coin] + 1)
            
            if cost != float("inf"):
                dp[target] = cost
       
        return dp[-1]