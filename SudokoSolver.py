def solve_sudoku(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j] == 0:
                for num in range(1, 10):
                    if is_valid_move(grid, i, j, num):
                        grid[i][j] = num

                        # print the grid after placing a number
                        print(f"Placed {num} at ({i}, {j})")
                        # for row in grid:
                        #     print(row)
                        # print("\n-----------------\n")
                        # for row in grid:
                        #     print(row)
                        # print("\n-----------------\n")

                        if solve_sudoku(grid):
                            return True

                        # undo the current cell for backtracking
                        grid[i][j] = 0

                return False
    return True

def find_empty_cell(grid):
    # Find the first empty cell in the grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                return row, col
    return -1, -1

def is_valid_move(grid, row, col, num):
    # Check if the number is already present in the same row
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check if the number is already present in the same column
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if the number is already present in the same 3x3 box
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False

    return True


