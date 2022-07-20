class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(subset, index):
            for i in range(index, len(nums)):
                subset.append(nums[i])
                results.append(subset[:])
                dfs(subset[:], i + 1)
                subset.pop()
            return
        
        results = [[]]
        dfs([], 0)
        return results