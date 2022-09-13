class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        '''
        Time Complexity is O(N)
        Space Complexity is O(N)
        '''
        
        answer = []
        
        p = 1
        for i in range(len(nums)):
            answer.append(p)
            p *= nums[i]
        
        p = 1
        for i in range(len(nums) - 1, -1, -1):
            answer[i] *= p
            p *= nums[i]
            
        return answer