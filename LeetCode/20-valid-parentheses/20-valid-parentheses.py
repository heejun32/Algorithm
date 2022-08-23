class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for character in s:
            if stack and character in brackets:
                if brackets[character] != stack[-1]:
                    return False
                else:
                    stack.pop()
                    continue
            stack.append(character)
    
        return len(stack) == 0