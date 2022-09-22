class Solution:
    def canPartition(self, nums: List[int]) -> bool: 
        # exception
        if sum(nums) % 2 == 1:
            return False
        
        target = sum(nums) // 2
        dp = [True] + [False] * target
        
        for num in nums:
            # 정답을 먼저 찾은 경우 남은 nums를 살펴볼 필요가 없다.
            if dp[-1]:
                break
            for i in range(len(dp) - 1, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]
                
        return dp[-1]