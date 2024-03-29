import collections


class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack, seen, counter = list(), set(), collections.Counter(s)
        for char in s:
            counter[char] -= 1
            
            if char in seen:
                continue
            
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            
            stack.append(char)
            seen.add(char)
        
        return ''.join(stack)
        