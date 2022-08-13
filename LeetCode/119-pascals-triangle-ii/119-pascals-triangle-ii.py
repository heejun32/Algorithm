class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        results = [[1]]
        for i in range(2, rowIndex + 2):
            rows = [1] * i
            for j in range(1, i - 1):
                rows[j] = results[-1][j - 1] + results[-1][j]
            results.append(rows) 
        return results[-1]