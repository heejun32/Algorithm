import collections


class Solution(object):
    def minimumRounds(self, tasks):
        """
        :type tasks: List[int]
        :rtype: int
        """
        counter = collections.Counter(tasks)
        # 예외 처리
        if 1 in counter.values():
            return -1
        
        rounds = 0
        for level in sorted(counter.keys()):
            while counter[level]:      
                # 2와 3의 배수가 아닐 경우, 3만큼 차감
                if counter[level] % 3 != 0 and counter[level] % 2 != 0:
                    counter[level] -= 3
                elif counter[level] % 3 == 0:
                    counter[level] -= 3
                elif counter[level] % 2 == 0:
                    counter[level] -= 2
                rounds += 1

        
        return rounds
            
        