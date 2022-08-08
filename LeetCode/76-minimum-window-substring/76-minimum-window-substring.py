class Solution(object):
    def minWindow(self, s, t):
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0
        
        for right, char in enumerate(s, 1):
            if need[char] > 0:
                missing -= 1
            need[char] -= 1
            # print(need)
                
            if missing == 0:
                while left <right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                    
                if not end or right -left <= end - start:
                    start, end = left, right
                    need[s[left]] += 1
                    missing += 1
                    left += 1

        return s[start: end]
    