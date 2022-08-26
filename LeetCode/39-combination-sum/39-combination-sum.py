class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(csum, index, path):
            if csum < 0:
                return None
            if csum == 0:
                results.append(path)
            
            
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path + [candidates[i]])
        
        results = []
        dfs(target, 0, [])
        
        return results