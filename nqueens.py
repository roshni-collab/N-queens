def solveNQueens(n):
    def is_safe(row, col):
        return col not in cols and (row - col) not in diagonal1 and (row + col) not in diagonal2