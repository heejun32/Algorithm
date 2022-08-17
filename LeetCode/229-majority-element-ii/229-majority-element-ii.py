class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        result = []
        for num, count in counter.items():
            if count > len(nums) / 3:
                result.append(num)
        return result
        