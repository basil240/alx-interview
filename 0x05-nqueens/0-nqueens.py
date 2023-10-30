#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    # Check if a queen can be placed in board[row][col]
    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)

    N = int(N)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = []
    solve_n_queens_util(board, 0, N, solutions)
    return solutions

def solve_n_queens_util(board, col, N, solutions):
    if col == N:
        solutions.append(format_solution(board))
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, N, solutions) or res
            board[i][col] = 0

    return res

def format_solution(board):
    N = len(board)
    formatted_solution = []
    for i in range(N):
        row = ''.join('Q' if board[i][j] == 1 else '.' for j in range(N))
        formatted_solution.append(row)
    return '\n'.join(formatted_solution)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solutions = solve_n_queens(sys.argv[1])
    for solution in solutions:
        print(solution)
