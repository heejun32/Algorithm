class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Exception
        if not s:
            return 0

        used = dict()
        start = max_lenght = 0
        for idx, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1
            else:
                max_lenght = max(max_lenght, idx - start + 1)
            used[char] = idx

        return max_lenght
