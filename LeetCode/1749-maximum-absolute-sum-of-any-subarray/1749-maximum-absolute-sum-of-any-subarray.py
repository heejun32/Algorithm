class Solution(object):
    def maxAbsoluteSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_s = min_s = largest_sum = 0
        for num in nums:
            max_s = max(max_s + num, 0)
            min_s = min(min_s + num, 0)            
            largest_sum = max(largest_sum, max_s, -min_s)            
            
        return largest_sum