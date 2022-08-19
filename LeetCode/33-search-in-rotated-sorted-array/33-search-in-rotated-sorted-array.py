class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 최솟값 index 찾기
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        
        # 최솟값 index 위치가 pivot
        pivot = left
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            pivot_mid = (mid + pivot) % len(nums)
            
            if nums[pivot_mid] < target:
                left = mid + 1
            elif nums[pivot_mid] > target:
                right = mid - 1
            else:
                return pivot_mid
        
        # 결과가 없다면
        return -1
                
        