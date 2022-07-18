from collections import Counter


class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewels_counter = Counter(jewels)
        answer = 0
        for stone in stones:
            if stone in jewels_counter:
                answer += 1
        return answer
