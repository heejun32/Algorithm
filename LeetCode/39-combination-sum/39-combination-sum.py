class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(comb, idx):
            # 초과 발생시 종료
            if sum(comb) > target:
                return
            # 조건 충족시 종료
            if sum(comb) == target:
                results.append(comb)
                return
            
            for i in range(idx, len(candidates)):
                comb.append(candidates[i])
                dfs(comb[:], i)
                comb.pop()
            return
        
        results = []
        dfs([], 0)
        return results