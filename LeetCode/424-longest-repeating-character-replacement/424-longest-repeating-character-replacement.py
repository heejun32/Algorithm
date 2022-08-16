class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        # max(right) - max(left) - max_char_n = k 이면 정답
        left = 0
        counter = collections.Counter()
        for right in range(1, len(s) + 1):
            counter[s[right - 1]] += 1
            max_char_n = counter.most_common(1)[0][1]
            
            if right - left - max_char_n > k:
                counter[s[left]] -= 1
                left += 1
        return right - left
            