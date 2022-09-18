class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def dfs(path):
            if len(path) == len(nums):
                answer.append(path)
                return None
            
            for i in range(len(nums)):
                if not visited[i]:
                    visited[i] = True
                    dfs(path + [nums[i]])
                    visited[i] = False
                
        answer = []
        visited = [False] * len(nums)
        dfs([])
        
        return answer