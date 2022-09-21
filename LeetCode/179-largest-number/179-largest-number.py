class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def to_swap(num1: int, num2: int) -> bool:
            return str(num1) + str(num2) < str(num2) + str(num1)
        
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and to_swap(nums[j - 1], nums[j]):
                nums[j - 1], nums[j] = nums[j], nums[j - 1]
                j -= 1
            i += 1
        
        return str(int(''.join(map(str, nums))))