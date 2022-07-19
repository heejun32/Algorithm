class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
#         def dfs(comb):
#             if len(comb) == len(nums):
#                 result.append(comb)
#                 return
#             for idx, num in enumerate(nums):
#                 if not visited[idx]:
#                     visited[idx] = True
#                     comb.append(num)
#                     dfs(comb[:])
#                     visited[idx] = False
#                     comb.pop()

#         visited = [False] * len(nums)
#         result = []
#         dfs([])
#         return result
        return list(map(list, itertools.permutations(nums)))