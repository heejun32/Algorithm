class Solution(object):
    def largestNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: str
        """
        # 같은 자리의 숫자면 큰 수가, 아니라면 작은 수가 앞에 올수록 최종 숫자의 크기가 크다.
        nums = list(map(str, nums))
        nums.sort(key=lambda x: x * 9, reverse=True)
        return str(int(''.join(nums)))
        