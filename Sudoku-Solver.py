# Function to print solved grid
def puzzle(a, m, n):
    for i in range(m):
        for j in range(n):
            print(a[i][j], end=" ")
        print()


# Function to check if num can be placed using Sudoku rules
def solve(grid, row, col, num, m, n, sub_m, sub_n):
    for x in range(n):
        if grid[row][x] == num:
            return False
    for x in range(m):
        if grid[x][col] == num:
            return False
    start_row, start_col = row - row % sub_m, col - col % sub_n
    for i in range(sub_m):
        for j in range(sub_n):
            if grid[i + start_row][j + start_col] == num:
                return False
    return True


# Backtracking function to solve Sudoku
def Sudoku(grid, row, col, m, n, sub_m, sub_n):
    if row == m - 1 and col == n:
        return True
    if col == n:
        row, col = row + 1, 0
    if grid[row][col] > 0:
        return Sudoku(grid, row, col + 1, m, n, sub_m, sub_n)
    for num in range(1, n + 1):
        if solve(grid, row, col, num, m, n, sub_m, sub_n):
            grid[row][col] = num
            if Sudoku(grid, row, col + 1, m, n, sub_m, sub_n):
                return True
        grid[row][col] = 0
    return False


# Give zero for empty cells, put each row in list, put all rows in nested list
grid = [
    [0, 0, 3, 0, 4, 0],
    [0, 0, 0, 0, 0, 5],
    [5, 0, 0, 2, 0, 0],
    [0, 0, 2, 0, 0, 6],
    [3, 0, 0, 0, 0, 0],
    [0, 6, 0, 3, 0, 0],
]

m = len(grid)  # no of rows
n = len(grid[0])  # no of cols
sub_m = 2  # no of rows in subgrid
sub_n = 3  # no of cols in subgrid

if Sudoku(grid, 0, 0, m, n, sub_m, sub_n):
    puzzle(grid, m, n)
else:
    print("No solution")
