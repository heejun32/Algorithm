class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_map = {}
        
        for i, num in enumerate(nums):
            nums_map[num] = i
            
        for i, num in enumerate(nums):
            if target - num in nums_map and nums_map[target - num] != i:
                return [i, nums_map[target - num]]