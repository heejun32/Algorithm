class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parentheses = {'(': ')', '[': ']', '{': '}'}
        for char in s:
            if char in parentheses:
                stack.append(char)
            else:
                if not stack or parentheses[stack.pop()] != char:
                    return False
        
        return len(stack) == 0
    # O(n)
    # 공간복잡도 n: s의 길이, k: 괄호의 종류 => O(n + k)