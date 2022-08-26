class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(elements, start, k):
            if k == 0:
                results.append(elements[:])
                return None
            
            for i in range(start, n + 1):
                elements.append(i)
                dfs(elements, i + 1, k - 1)
                elements.pop()
        
        results = []
        dfs([], 1, k)
        
        return results