class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        volume = 0
        
        while left < right:
            volume = max(volume, (right - left) * min(height[left], height[right]))
            
            if height[left] >= height[right]:
                right -= 1
            else:
                left += 1
                
        return volume
            