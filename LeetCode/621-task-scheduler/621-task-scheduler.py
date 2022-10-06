import collections


class Solution:
    '''
    Time Complexity is O(N)
    Space Complexity is O(26) -> O(1)
    '''
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = collections.Counter(tasks)
        result = 0

        while True:
            # 부분 작업 시간
            sub_count = 0

            # 개수 순 추출
            for task, _ in counter.most_common(n + 1):
                sub_count += 1
                result += 1

                counter[task] -= 1
                # 0 이하인 아이템을 목록에서 완전히 제거
                counter += collections.Counter()

            if not counter:
                break

            # idle 없이 작업이 가능한지 계산
            result += n + 1 - sub_count

        return result
