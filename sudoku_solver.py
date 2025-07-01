# sudoku_solver.py

def get_user_board():
    print("Enter your Sudoku puzzle row by row (use 0 for empty cells):")
    board = []
    for i in range(9):
        while True:
            try:
                row = input(f"Row {i+1}: ").strip().split()
                if len(row) != 9:
                    raise ValueError("Each row must have 9 numbers.")
                row = [int(num) for num in row]
                if any(num < 0 or num > 9 for num in row):
                    raise ValueError("Numbers must be between 0 and 9.")
                board.append(row)
                break
            except ValueError as ve:
                print("Invalid input:", ve)
    return board


def print_board(b):
    for i in range(len(b)):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(len(b[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(b[i][j])
            else:
                print(str(b[i][j]) + " ", end="")


def find_empty(b):
    for i in range(len(b)):
        for j in range(len(b[0])):
            if b[i][j] == 0:
                return (i, j)  # row, col
    return None


def is_valid(b, num, pos):
    row, col = pos

    # Check row
    for i in range(len(b[0])):
        if b[row][i] == num and col != i:
            return False

    for i in range(len(b)):
        if b[i][col] == num and row != i:
            return False

    box_x = col // 3
    box_y = row // 3

    for i in range(box_y * 3, box_y * 3 + 3):
        for j in range(box_x * 3, box_x * 3 + 3):
            if b[i][j] == num and (i, j) != pos:
                return False

    return True


def solve(b):
    find = find_empty(b)
    if not find:
        return True  # Solved
    else:
        row, col = find

    for i in range(1, 10):
        if is_valid(b, i, (row, col)):
            b[row][col] = i

            if solve(b):
                return True

            b[row][col] = 0

    return False

board = get_user_board()

print("\nOriginal Sudoku:")
print_board(board)

if solve(board):
    print("\nSolved Sudoku:")
    print_board(board)
else:
    print("\nNo solution exists")
