class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 예외처리
        if len(nums) <= 2:
            return max(nums)
        
        # 초기갑 설정
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        answer = float('-inf')
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + dp[i - 2])
            answer = max(answer, dp[i])
        return answer
            