class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        brackets = {')': '(', '}': '{', ']': '['}
        stack = []
        
        for character in s:
            # stack이 비어있지 않고, key 값의 괄호가 들어오면 비교
            if stack and character in brackets:
                # 다를 경우 not valid pare, return False
                if brackets[character] != stack[-1]:
                    return False
                # 같을 경우 stack의 마지막 원소 pop뒤 다음 원소 확인
                else:
                    stack.pop()
                    continue
            stack.append(character)
    
        # 모든 탐새을 마치고 스택이 비어있는지 확인
        return len(stack) == 0