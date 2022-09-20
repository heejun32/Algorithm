class Solution:
    '''
    Time Complexity is O(2 ^ N)
    Space Complexity is O(2 ^ N)

    '''
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(start, path):
            answer.append(path)
            
            for i in range(start, len(nums)):
                dfs(i + 1, path + [nums[i]])
        
        answer = []
        dfs(0, [])
        
        return answer