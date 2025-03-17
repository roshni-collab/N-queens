def solveNQueens(n):
    def is_safe(row, col):
        return col not in cols and (row - col) not in diagonal1 and (row + col) not in diagonal2
    
    def solve_n_queens(row):
        if row == n:
            board = ["".join(row) for row in chessboard]
            solutions.append(board)
            return
        
        for col in range(n):
            if is_safe(row, col):
                 # Place the queen
                chessboard[row][col] = 'Q'
                cols.add(col)
                diagonal1.add(row - col)
                diagonal2.add(row + col) 