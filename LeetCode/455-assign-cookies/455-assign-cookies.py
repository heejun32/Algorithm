class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        g.sort()
        s.sort()
        answer = 0
        left = 0
        for i in range(len(g)):
            while left < len(s):
                if g[i] <= s[left]:
                    answer += 1
                    left += 1
                    break
                left += 1
        return answer