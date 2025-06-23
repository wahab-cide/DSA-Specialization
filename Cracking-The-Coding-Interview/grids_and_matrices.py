"""
Given a grid, room, and a player's position {r, c}, what are the immediately available ceels they can move to.

Each cell can be either an obstacle(1) or a walkable space(0).
"""

class Solution:
    def valid_Moves(self, room, r, c):


        moves = []
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        for dir_r, dir_c in dirs:
            new_r, new_c = r + dir_r, c + dir_c
            if self.is_valid(room, new_r, new_c):
                moves.append([new_r, new_c])

        return moves

    def is_valid(self, room, r, c):
        return 0 <= r < len(room) and 0 <= c < len(room[0] and room[r, c] != 1)
    

"""
Chess moves:

Given a chess board, a piece(knight, queen, or king), and a position {r, c}, what are the immediately available cells it can move to.

Each cell can be either an obstacle(1) or a walkable space(0).
"""
class Solution:
    def reachable_cells(self, board, piece, r, c):
        moves = []

        king_directions = [[1, 0], [-1, 0], [0, -1], [0, 1], [1, 1], [1, -1], [-1, 1], [-1, -1]]
        knight_directions = [[2, 1], [-2, 1], [2, -1], [-2, -1], [1, 2], [1, -2], [-1, 2], [-1, -2]]

        if piece == 'knight':
            directions = knight_directions
        else:
            directions = king_directions

        for dir_r, dir_c in directions:
            new_r, new_c = r + dir_r, c + dir_c

            if piece == 'queen':
                while self.is_valid(board, new_r, new_c):
                    moves.append([new_r, new_c])
                    new_r += dir_r
                    new_c += dir_c

            elif self.is_valid(board, new_r, new_c):
                moves.append([new_r, new_c])
        return moves

    def is_valid(self, board, r, c):
        return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != 1




"""
Chess moves: All pieces
"""
class Solution:
    def reachable_cells(self, board, piece, r, c):
        moves = []

        directions_map = {
            'king': [[1, 0], [-1, 0], [0, -1], [0, 1],
                     [1, 1], [1, -1], [-1, 1], [-1, -1]],
            'knight': [[2, 1], [-2, 1], [2, -1], [-2, -1],
                       [1, 2], [1, -2], [-1, 2], [-1, -2]],
            'rook': [[1, 0], [-1, 0], [0, -1], [0, 1]],
            'bishop': [[1, 1], [1, -1], [-1, 1], [-1, -1]],
            'queen': [[1, 0], [-1, 0], [0, -1], [0, 1],
                      [1, 1], [1, -1], [-1, 1], [-1, -1]],
            'pawn': [[-1, 0]]  # Always upward in this simplified model
        }

        sliding_pieces = {'queen', 'rook', 'bishop'}

        if piece not in directions_map:
            return moves

        for dir_r, dir_c in directions_map[piece]:
            new_r, new_c = r + dir_r, c + dir_c

            while self.is_valid(board, new_r, new_c):
                moves.append([new_r, new_c])
                if piece in sliding_pieces:
                    new_r += dir_r
                    new_c += dir_c
                else:
                    break

        return moves

    def is_valid(self, board, r, c):
        return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == 0



"""
Queen's Reach
"""
class Solution:
    def queens_reach(self, board):
        n = len(board)
        res = [[0] * n for _ in range(n)]

        for r in range(n):
            for c in range(n):
                if board[r][c] == 1:
                    res[r][c] = 1
                    self.mark_queen_reaches(board, res, r, c)
        return res

    def mark_queen_reaches(self, board, res, r, c):
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]

        for dir_r, dir_c in dirs:
            new_r, new_c = r + dir_r, c + dir_c
            while self.is_valid(board, new_r, new_c):
                res[new_r][new_c] = 1
                new_r += dir_r
                new_c += dir_c

    def is_valid(self, board, r, c):
        return 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] != 1
    

from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[int]]) -> bool:
        return (
            self.valid_rows(board) and 
            self.valid_columns(board) and 
            self.valid_subgrids(board)
        )

    def valid_rows(self, board):
        for r in range(len(board)):
            seen = set()
            for c in range(len(board[0])):
                if board[r][c] != 0:
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])
        return True

    def valid_columns(self, board):
        transposed = [list(row) for row in zip(*board)]
        for r in range(len(transposed)):
            seen = set()
            for c in range(len(transposed[0])):
                if transposed[r][c] != 0:
                    if transposed[r][c] in seen:
                        return False
                    seen.add(transposed[r][c])
        return True

    def valid_subgrids(self, board):
        for r in range(3):
            for c in range(3):
                if not self.valid_subgrid(board, r * 3, c * 3):
                    return False
        return True

    def valid_subgrid(self, board, r, c):
        seen = set()
        for nr in range(r, r + 3):
            for nc in range(c, c + 3):
                if board[nr][nc] != 0:
                    if board[nr][nc] in seen:
                        return False
                    seen.add(board[nr][nc])
        return True


board = [
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

sol = Solution()
print(sol.isValidSudoku(board))  # Output: True
