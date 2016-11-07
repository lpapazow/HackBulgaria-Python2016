from fractions import Fraction
CONST_LIST = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def rows_ok(sudoku):
    for row in sudoku:
        if sorted(row) != CONST_LIST:
            return False
    return True


def cols_ok(sudoku):
    for j in range(len(sudoku)):
        col = [None] * 9
        for i in range(len(sudoku[1])):
            col[i] = sudoku[i][j]
        if sorted(col) != CONST_LIST:
            return False
    return True


def squares_ok(sudoku):
    for hor_sqr in range(3):
        for ver_sqr in range(3):
            current_sqr = []
            for i in range(3):
                for j in range(3):
                    current_sqr.append(sudoku[(hor_sqr * 3) + i][(ver_sqr * 3) + j])
            if sorted(current_sqr) != CONST_LIST:
                return False
    return True


def sudoku_solved(sudoku):
    return squares_ok(sudoku) and cols_ok(sudoku) and rows_ok(sudoku)
