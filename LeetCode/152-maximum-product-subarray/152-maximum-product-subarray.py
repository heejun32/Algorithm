class Solution:
    '''
    Time Complexity is O(N)
    Space Compexity is O(1)
    '''
    def maxProduct(self, nums: List[int]) -> int:
        max_pro = min_pro = answer = nums[0]
        
        for i in range(1, len(nums)):
            max_pro, min_pro = max(nums[i], max_pro * nums[i], min_pro * nums[i]), min(nums[i], max_pro * nums[i], min_pro * nums[i])
            answer = max(answer, max_pro)
            
        return answer