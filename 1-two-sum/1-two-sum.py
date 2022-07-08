class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for i in range(len(nums)):
            rest = target - nums[i]
            if rest in hash_map:
                return [i, hash_map[rest]]
            hash_map[nums[i]] = i