def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def is_valid_move(board, row, col, num):
    # Check the row for duplicates
    if num in board[row]:
        return False

    # Check the column for duplicates
    if num in [board[i][col] for i in range(9)]:
        return False

    # Check the 3x3 grid for duplicates
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

# Ask the user if they want to create a custom Sudoku board
user_choice = input("Do you want to create a custom Sudoku board? (yes/no): ")

if user_choice.lower() == "yes":
    # Create a custom Sudoku board
    sudoku_board = [[0 for _ in range(9)] for _ in range(9)]
    print("Enter the Sudoku board values row by row (use 0 for empty cells):")
    for i in range(9):
        while True:
            row_values = input(f"Enter values for row {i + 1} (9 numbers separated by spaces): ").split()
            if len(row_values) == 9:
                break
            else:
                print("Please enter 9 values.")
        sudoku_board[i] = [int(val) for val in row_values]
else:
    # Use the default Sudoku board
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

if solve_sudoku(sudoku_board):
    print("Solved Sudoku:")
    print_board(sudoku_board)
else:
    print("No solution exists.")
