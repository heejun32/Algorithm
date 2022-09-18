class Solution:
    '''
    Time Complexity is O(N! / ((N - K)!K!))
    Space Complexity is O(N! / ((N - K)!K!))

    '''
    def combine(self, n: int, k: int) -> List[List[int]]:
        def dfs(start, path):
            if len(path) == k:
                answer.append(path)
                return None
            
            for i in range(start, n + 1):
                dfs(i + 1, path + [i])
                
        answer = []
        dfs(1, [])
        
        return answer