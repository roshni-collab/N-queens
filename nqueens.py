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

                # Recurse to the next row
                solve_n_queens(row + 1)

                # Backtrack: Remove the queen
                chessboard[row][col] = '.'
                cols.remove(col)
                diagonal1.remove(row - col)
                diagonal2.remove(row + col)
    
    # Initialize variables
    solutions = []
    chessboard = [['.'] * n for _ in range(n)]
    cols, diagonal1, diagonal2 = set(), set(), set()

    # Start solving from the first row
    solve_n_queens(0)

    return solutions

# Example Test Cases
print(solveNQueens(4))
print(solveNQueens(1))