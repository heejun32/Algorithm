class Solution(object):
    def dailyTemperatures(self, t):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        answer = [0] * len(t)
        stack = []
        for i, cur in enumerate(t):
            while stack and cur > t[stack[-1]]:
                last = stack.pop()
                answer[last] = i - last
            stack.append(i)
            
        return answer
                