class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)
        
        while white < blue:
            if nums[white] > 1:
                blue -= 1
                nums[white], nums[blue] = nums[blue], nums[white]
            elif nums[white] < 1:
                nums[white], nums[red] = nums[red], nums[white]
                white += 1
                red += 1
            else:
                white += 1