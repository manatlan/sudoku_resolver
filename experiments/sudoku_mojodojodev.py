#!./make.py

#INFO: another algo from mojodojo.dev (100grids)

import time

"""python version from https://mojodojo.dev/guides/benchmarks/sudoku.html """

def is_valid(board, row, col, num):
    for x in range(9):
        if board[row][x] == num:
            return False

    for x in range(9):
        if board[x][col] == num:
            return False

    start_row = row - row % 3
    start_col = col - col % 3
    for i in range(3):
        for j in range(3):
            if board[i+start_row][j+start_col] == num:
                return False
    return True

def solve_sudoku(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                for num in range(1, 10):
                    if is_valid(board, i, j, num):
                        board[i][j] = num
                        if solve_sudoku(board):
                            return True
                        board[i][j] = 0
                return False
    return True

if __name__=="__main__":
    gg = [i.strip() for i in open("grids.txt")][:100]

    # convert my grids into mojodojodev'boards -> boards
    boards=[]
    for g in gg:
        board=[]
        for x in range(0,81,9):
            board.append( [ (0 if i=="." else ord(i)-48) for i in g[x:x+9]])
        boards.append( board )

    t=time.monotonic()
    for board in boards:
        solve_sudoku(board)
        print(board)
    print( "Took: ", time.monotonic() - t )

