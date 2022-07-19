class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
#         def dfs(start, comb):
#             if len(comb) == k:
#                 result.append(comb)
#                 return
            
#             for number in range(start, n + 1):
#                 comb.append(number)
#                 dfs(number + 1, comb[:])
#                 comb.pop()
        
#         result = []
#         dfs(1, [])
#         return result
        return list(map(list, itertools.combinations(range(1, n + 1), k)))