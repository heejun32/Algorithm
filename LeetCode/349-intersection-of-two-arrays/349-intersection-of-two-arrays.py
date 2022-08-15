class Solution(object):
    def intersection(self, nums1, nums2):
        nums1 = sorted(set(nums1))
        nums2 = sorted(set(nums2))
        
        result = []
        for target in nums1:
            left, right = 0 , len(nums2) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums2[mid] < target:
                    left = mid + 1
                elif nums2[mid] > target:
                    right = mid - 1
                else:
                    result.append(target)
                    break
        return result
        