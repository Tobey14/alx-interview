#!/usr/bin/python3
"""0-nqueens module that solves the N queens problem
"""
import sys

def is_safe(board, row, col, N):
    """is_safe function that checks if a queen can be placed on board

    Args:
        board (list): board list
        row (int): row number
        col (int): column number
        num (int): number of queens in board

    Returns:
        bool: True if safe, False otherwise
    """
    for i in range(col):
        if board[row][i] == 1:
            return False
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True

def solve_nqueens(N):
    """solve_nqueens function that solves the N queens problem

    Args:
        board (list): board list
        col (int): column number
        num (int): number of queens in board

    Returns:
        bool: True if safe, False otherwise
    """
    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens_util(board, 0, N):
        print("Solution does not exist")
        return False
    print_solution(board, N)
    return True

def solve_nqueens_util(board, col, N):
    """function that contributes to solve the N queens problem

    Args:
        num (int): number of queens
    """
    if col >= N:
        return True
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            if solve_nqueens_util(board, col + 1, N):
                return True
            board[i][col] = 0
    return False

def print_solution(board, N):
    """function that solves the N queens problem

    Args:
        num (int): number of queens
    """
    for i in range(N):
        for j in range(N):
            print(board[i][j], end=" ")
        print()

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python nqueens.py N")
    else:
        try:
            N = int(sys.argv[1])
            solve_nqueens(N)
        except ValueError:
            print("N must be a valid integer")
