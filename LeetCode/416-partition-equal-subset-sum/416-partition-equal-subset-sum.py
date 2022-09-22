class Solution:
    def canPartition(self, nums: List[int]) -> bool: 
        # exception
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        dp = [True] + [False] * target
        
        for num in nums:
            if dp[-1]:
                break
            for i in range(len(dp) - 1, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                
        return dp[-1]