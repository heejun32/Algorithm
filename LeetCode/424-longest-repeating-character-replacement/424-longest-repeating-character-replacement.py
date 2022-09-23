import collections


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        max_len = float('-inf')
        counts = collections.Counter()
        
        for right in range(1, len(s) + 1):
            counts[s[right - 1]] += 1
            
            # 가장 흔하게 등장하는 단어 탐색
            max_char_n = counts.most_common(1)[0][1]
            
            if right - left - max_char_n <= k:
                max_len = max(max_len, right - left)
            
            if right - left - max_char_n > k:
                counts[s[left]] -= 1
                left += 1

        return max_len