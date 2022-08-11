class Solution:
    def diffWaysToCompute(self, expression):
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l) + op + str(r)))
            return results

        # 재귀 종료 조건
        if expression.isdigit():
            return [int(expression)]

        # 재귀 탐색 시작
        results = []
        for index, value in enumerate(expression):
            if value in "-+*":
                left = self.diffWaysToCompute(expression[:index])
                right = self.diffWaysToCompute(expression[index + 1:])

                results.extend(compute(left, right, value))
                # print(results)
        return results