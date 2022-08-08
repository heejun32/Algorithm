import collections


class Solution:
    def minWindow(self, s, t):
        need = collections.Counter(t)
        missing = len(t)
        left = start = end = 0

        # 오른쪽 포인터 이동: 인덱스는 0이 아닌 1이 시작점, 값이 변하진 않음.
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1

            # 필요 문자가 0이면 왼쪽 포인터 이동 판단
            if missing == 0:
                # print(s[left: right])
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                # 조건을 만족하고, 부분 문자열의 길이가 가장 짧은 값으로 초기화
                if not end or right - left <= end - start:
                    start, end = left, right
                # 조건을 깨주고 다시 탐색 시작
                need[s[left]] += 1
                missing += 1
                left += 1
        return s[start:end]
