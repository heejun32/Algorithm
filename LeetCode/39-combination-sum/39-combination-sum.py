class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(csum, start, path):
            if csum < 0:
                return None
            if csum == 0:
                answer.append(path)
            
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                dfs(csum - candidates[i], i, path[:])
                path.pop()
        
        answer = []
        dfs(target, 0, [])
        
        return answer
            