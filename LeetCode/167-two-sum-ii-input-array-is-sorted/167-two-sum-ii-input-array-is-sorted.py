class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(numbers)):
            rested = target - numbers[i]
            left, right = i + 1, len(numbers) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < rested:
                    left = mid + 1
                elif numbers[mid] > rested:
                    right = mid - 1
                else:
                    return [i + 1, mid + 1]