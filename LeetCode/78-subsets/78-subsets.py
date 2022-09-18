class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path):
            answer.append(path)
            
            for i in range(start, len(nums)):
                path.append(nums[i])
                dfs(i + 1, path[:])
                path.pop()
                
        answer = []
        dfs(0, [])
        
        return answer