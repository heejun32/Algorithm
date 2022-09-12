# class Solution:
#     def coinChange(self, coins: List[int], amount: int) -> int:
#         dp = [0] + [-1] * (amount)
        
#         for target in range(amount + 1):
#             if dp[target] != -1:
#                 continue
            
#             cost = float("inf")
#             for coin in coins:
#                 if target - coin < 0 or dp[target - coin] == -1:
#                     continue
#                 cost = min(cost, dp[target - coin] + 1)
            
#             if cost != float("inf"):
#                 dp[target - coin] = cost
#         print(dp)            
#         return dp[-1]

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [-1] * (amount + 1)
        dp[0] = 0
        
        for idx in range(amount + 1):
            m = 987654321
            if dp[idx] != -1:
                continue
            for i in coins:
                x = idx - i
                if x < 0 or dp[x] == -1:
                    continue
                m = min(m, dp[x] + 1)
    
            dp[idx] = -1 if m == 987654321 else m
        
        return dp[amount]