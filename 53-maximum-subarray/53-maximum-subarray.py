class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [nums[0]] * len(nums)
        answer = dp[0]
        
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1] + nums[i], nums[i])
            answer = max(answer, dp[i])
        return answer
        