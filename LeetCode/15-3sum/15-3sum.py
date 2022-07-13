class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        answer = []
        nums.sort()
        
        for i in range(len(nums) - 2):
            
            # pass the duplicated values
            if i > 0 and nums[i - 1] == nums[i]:
                continue
            
            # two pointer
            left, right = i + 1, len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    
                    # pass the duplicated values
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
            
        return answer
