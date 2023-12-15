def is_valid(board, row, col, num):
    # Check if 'num' is not in the current row, column, and 3x3 grid
    for i in range(9):
        if (
            board[row][i] == num
            or board[i][col] == num
            or board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num
        ):
            return False
    return True


def find_empty_location(board):
    # Find the first empty cell in the board
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return i, j
    return None, None  # No empty cell found, puzzle is solved


def solve_sudoku(board):
    stack = []
    stack.append(board)

    while stack:
        current_board = stack.pop()
        row, col = find_empty_location(current_board)

        # Base case: if there is no empty cell, the puzzle is solved
        if row is None and col is None:
            return current_board

        # Try placing numbers 1 to 9 in the current empty cell
        for num in range(1, 10):
            if is_valid(current_board, row, col, num):
                # Make the choice
                new_board = [row[:] for row in current_board]
                new_board[row][col] = num
                stack.append(new_board)

    return None  # No solution exists


# Example usage
sudoku_board = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 0, 2, 8, 0],
    [0, 0, 0, 4, 1, 9, 0, 0, 5],
    [0, 0, 0, 0, 8, 0, 0, 7, 9],
]

solution = solve_sudoku(sudoku_board)

if solution:
    for row in solution:
        print(row)
else:
    print("No solution exists.")
