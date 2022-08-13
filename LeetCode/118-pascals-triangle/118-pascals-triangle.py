class Solution(object):
    def generate(self, numRows):
        results = []
        for i in range(1, numRows + 1):
            # 각 층 리스트 초기화
            rows = []
            for j in range(i):
                if j == 0 or j == i - 1:
                    rows.append(1)
                    continue
                # print(i, j)
                rows.append(results[i - 2][j - 1] + results[i - 2][j])
            results.append(rows)
        return results
            