import collections


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        
        p_counter = collections.Counter(p)
        s_counter = collections.Counter(s[:len(p) - 1])
        
        for i in range(len(p) - 1, len(s)):
            # window에 추가
            s_counter[s[i]] += 1
            
            # 정답 확인
            if p_counter == s_counter:
                output.append(i - len(p) + 1)
            
            s_counter[s[i - len(p) + 1]] -= 1
            if not s_counter[s[i - len(p) + 1]]:
                del s_counter[s[i - len(p) + 1]]
        
        return output