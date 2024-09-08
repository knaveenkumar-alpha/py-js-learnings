def solve_sudoku(board):
    def is_valid(num, pos):
        for i in range(9):
            if board[pos[0]][i] == num or board[i][pos[1]] == num:
                return False
        box_x, box_y = pos[1]//3, pos[0]//3
        for i in range(box_y*3, box_y*3+3):
            for j in range(box_x*3, box_x*3+3):
                if board[i][j] == num:
                    return False
        return True
    
    def solve():
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":
                    for num in map(str, range(1,10)):
                        if is_valid(num, (i,j)):
                            board[i][j] = num
                            if solve():
                                return True
                            board[i][j] = "."
                    return False
        return True
    solve()
    return board 


# Example usage:
board = [
    ["5", "3", ".", ".", "7", ".", ".", ".", "."],
    ["6", ".", ".", "1", "9", "5", ".", ".", "."],
    [".", "9", "8", ".", ".", ".", ".", "6", "."],
    ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
    ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
    ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
    [".", "6", ".", ".", ".", ".", "2", "8", "."],
    [".", ".", ".", "4", "1", "9", ".", ".", "5"],
    [".", ".", ".", ".", "8", ".", ".", "7", "9"]
]
# print(board)
solved_board = solve_sudoku(board)
for row in solved_board:
    print(row)
                            
print("========================================== N-Queens =================================")

def solveNQueens(n):
    def is_not_under_attack(row, col):
        for prev_row in range(row):
            if queens[prev_row] == col or \
               queens[prev_row] - prev_row == col - row or \
               queens[prev_row] + prev_row == col + row:
                return False
        return True

    def place_queen(row):
        for col in range(n):
            if is_not_under_attack(row, col):
                queens[row] = col
                if row + 1 == n:
                    result.append(queens[:])
                else:
                    place_queen(row + 1)

    result = []
    queens = [-1] * n
    place_queen(0)
    return [['.' * col + 'Q' + '.' * (n - col - 1) for col in sol] for sol in result]

# Example usage:
n = 4
solutions = solveNQueens(n)
for solution in solutions:
    for row in solution:
        print(row)
    print()
