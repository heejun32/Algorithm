class Solution:
    '''
    Time Complexity is O(NM)
    Space Complexity is O(NM)
    N is digits.lengh
    M is digit's range
    '''    
    def letterCombinations(self, digits: str) -> List[str]:
        # exception
        if not digits:
            return []

        letters = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"], 
                   "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                   "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        answer = []

        def dfs(idx, path):
            if len(path) == len(digits):
                answer.append(path)
                return None
            
            for i in range(idx, len(digits)):
                for char in letters[digits[i]]:
                    dfs(i + 1, path + char)

        dfs(0, "")
 
        return answer
