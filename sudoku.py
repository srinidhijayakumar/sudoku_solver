sudoku_grid = [
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

def print_sudoku(grid):
    for row in grid:
        print(" ".join(str(cell) if cell != 0 else '_' for cell in row))

print_sudoku(sudoku_grid)
def is_valid (grid,row,column,number):
    #column
    for c in range(len(grid[0])):
        if number == grid[c][column]:
            return False
    #row 
    if number in grid[row]:
        return  False
    #small grid 3*3
    s_row = (row//3)*3 #for finding the rightmost boxe's row
    s_column =(column//3)*3#to find the rightmost boxe's column
    for i in range(s_row,s_row+3):
        for j in range(s_column,s_column+3):
             if grid[i][j]==number:
                 return False
    return True #if none of these then the position and number are valid

def solve(grid):
    for i in range(9):
        for j in range(9):
            if grid[i][j]==0:# find an empty grid
                for num in range(1,10):
                    if is_valid(grid,i,j,num):# checking for validity
                        grid[i][j]=num
                        if solve(grid): # if not valid the val os not assigned to the box
                            return True
                        grid[i][j]=0# it is set to zero again so the box goes into the loop and passes the if empty condition. This is called backtracking.
                return False
    return True
                

solve(sudoku_grid)
print_sudoku(sudoku_grid)
    

