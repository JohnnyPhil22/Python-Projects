m=9
def puzzle(a):
    for i in range(m):
        for j in range(m):
            print(a[i][j],end=' ')
        print()
def solve(grid,row,col,num):
    for x in range(9):
        if grid[row][x]==num:
            return False
    for x in range(9):
        if grid[x][col]==num:
            return False
    start_row,start_col=row-row%3,col-col%3
    for i in range(3):
        for j in range(3):
            if grid[i+start_row][j+start_col]==num:
                return False
    return True
def Sudoku(grid,row,col):
    if row==m-1 and col==m:
        return True
    if col==m:
        row,col=row+1,0
    if grid[row][col]>0:
        return Sudoku(grid,row,col+1)
    for n in range(1,m+1,1):
        if solve(grid,row,col,n):
            grid[row][col]=n
            if Sudoku(grid,row,col+1):
                return True
        grid[row][col]=0
    return False

# Give zero for empty cells, put each row in list, put all rows in nested list
grid=[[0,0,1,0,6,0,0,0,0],
    [0,0,0,0,0,0,2,3,8],
    [0,7,0,2,0,0,0,4,0],
    [7,0,0,0,0,6,0,0,0],
    [0,9,3,1,4,0,5,0,0],
    [0,8,0,0,5,0,0,0,4],
    [0,3,0,0,7,0,8,0,0],
    [0,6,5,4,1,0,0,0,2],
    [2,0,0,0,0,3,0,0,0]]

if Sudoku(grid,0,0):
    puzzle(grid)
else:
    print('No solution')