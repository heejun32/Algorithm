class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row_start = col_start = 0
        row_end, col_end = len(matrix) - 1, len(matrix[0]) - 1
        order = list()
        
        while row_start <= row_end and col_start <= col_end:
            for col in range(col_start, col_end + 1):
                order.append(matrix[row_start][col])
            row_start += 1
            
            for row in range(row_start, row_end + 1):
                order.append(matrix[row][col_end])
            col_end -= 1
            
            if row_start <= row_end:
                for col in range(col_end, col_start - 1, -1):
                    order.append(matrix[row_end][col])
                row_end -= 1
            
            if col_start <= col_end:
                for row in range(row_end, row_start -1, -1):
                    order.append(matrix[row][col_start])
                col_start += 1
            
        return order