class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        def dfs(index, path):
            if len(path) == len(digits):
                results.append(path)
                return None
            
            for i in range(index, len(digits)):
                for j in mapping_digits[digits[i]]:
                    dfs(i + 1, path + j)
                    
        # 예외처리
        if not digits:
            return []
        
        mapping_digits = {"2": ["a", "b", "c"], "3": ["d", "e", "f"], "4": ["g", "h", "i"],
                  "5": ["j", "k", "l"], "6": ["m", "n", "o"], "7": ["p", "q", "r", "s"],
                  "8": ["t", "u", "v"], "9": ["w", "x", "y", "z"]}
        
        results = []
        dfs(0, "")
        
        return results
    