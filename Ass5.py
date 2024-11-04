def solveNQueens1(n: int, first_queen_col: int):
    col = set()
    posDiag = set()  # positive diagonals (r + c)
    negDiag = set()  # negative diagonals (r - c)
    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "Q"

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    # Place the first queen in the specified column of the first row
    col.add(first_queen_col)
    posDiag.add(0 + first_queen_col)
    negDiag.add(0 - first_queen_col)
    board[0][first_queen_col] = "Q"

    # Start backtracking from the second row
    backtrack(1)
    return res

def solveNQueens2(n: int, first_queen_col: int):
    col = set()
    posDiag = set()
    negDiag = set()
    res = []
    board = [["."] * n for _ in range(n)]

    def backtrack(r):
        if r == n:
            res.append(["".join(row) for row in board])
            return
        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue
            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "I"  # Replace "Q" with "I" for this version

            backtrack(r + 1)

            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "."

    # Place the first queen in the specified column of the first row
    col.add(first_queen_col)
    posDiag.add(0 + first_queen_col)
    negDiag.add(0 - first_queen_col)
    board[0][first_queen_col] = "I"  # Replace "Q" with "I" for this version

    # Start backtracking from the second row
    backtrack(1)
    return res

if __name__ == "__main__":
    n = 8
    first_queen_col = 1

    # Solution with "Q" for queens
    board = solveNQueens1(n, first_queen_col)[0]
    for row in board:
        print(" ".join(row))

    print("\nWe Replace 'Q' by 'I'\n")

    # Solution with "I" for queens
    board = solveNQueens2(n, first_queen_col)[0]
    for row in board:
        print(" ".join(row))
