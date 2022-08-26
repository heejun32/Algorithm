class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(permu):
            if len(permu) == len(nums):
                result.append(permu)
                return
            for idx, num in enumerate(nums):
                if not visited[idx]:
                    visited[idx] = True
                    permu.append(num)
                    dfs(permu[:])
                    visited[idx] = False
                    permu.pop()

                    
        visited = [False] * len(nums)
        result = []
        dfs([])
        return result
