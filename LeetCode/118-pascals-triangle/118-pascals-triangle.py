class Solution(object):
    def generate(self, numRows):
        results = [[1]]
        for i in range(2, numRows + 1):
            # 각 층 리스트 초기화
            rows = [1] * i
            for j in range(1, i - 1):
                rows[j] = results[-1][j - 1] + results[-1][j]
            results.append(rows)
        return results
            