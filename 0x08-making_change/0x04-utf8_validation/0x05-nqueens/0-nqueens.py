#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if there is a queen in the same column
    for i in range(row):
        if board[i] == col or board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True

def solve_nqueens(n, row, board, solutions):
    if row == n:
        # Found a solution, append a copy of the board to solutions
        solutions.append([i for i in board])
        return

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_nqueens(n, row + 1, board, solutions)

def print_solutions(solutions):
    for solution in solutions:
        print([[i, solution[i]] for i in range(len(solution))])

def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [-1] * N
    solutions = []
    solve_nqueens(N, 0, board, solutions)
    print_solutions(solutions)

if __name__ == "__main__":
    main()
