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


"""
Sudoku Solver
"""
from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.backtrack(board)

    def backtrack(self, board) -> bool:
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':  # ✅ Only process empty cells
                    for num in map(str, range(1, 10)):
                        if self.is_valid(board, i, j, num):
                            board[i][j] = num
                            if self.backtrack(board):
                                return True
                            board[i][j] = '.'  # Backtrack
                    return False  # No valid number found (trigger backtracking)
        return True  # All cells filled (solution found)

    def is_valid(self, board, r, c, num) -> bool:
        # Check row
        for i in range(9):
            if board[r][i] == num:
                return False
        
        # Check column
        for i in range(9):
            if board[i][c] == num:
                return False
        
        # Check 3×3 box
        sr, sc = 3 * (r // 3), 3 * (c // 3)
        for i in range(sr, sr + 3):
            for j in range(sc, sc + 3):
                if board[i][j] == num:  # ✅ Check all box cells
                    return False
        
        return True  # Number is valid



"""Rotate Image
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.
"""

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        for i in range(n):
            for j in range(i, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        for i in range(n):
            matrix[i].reverse()



"""
Spiral Matrix
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:

        m, n = len(matrix), len(matrix[0])
        top, bottom = 0, m - 1
        left, right = 0, n - 1
        res = []

        while top <= bottom and left <= right:

            for i in range(left, right + 1):
                res.append(matrix[top][i])
            top += 1

            for i in range(top, bottom + 1):
                res.append(matrix[i][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(matrix[i][left])
                left += 1

        return res

"""
Unique Paths II

ou are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [[0] * n for _ in range(m)]
        dp[0][0] = 1

        #for columns
        for i in range(1, m):
            if obstacleGrid[i][0] == 0:
                dp[i][0] = dp[i - 1][0]
            else:
                dp[i][0] = 0
        #for cols
        for i in range(1, n):
            if obstacleGrid[0][i] == 0:
                dp[0][i] = dp[0][i - 1]
            else:
                dp[0][i] = 0

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 0:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                else:
                    dp[i][j] = 0

        return dp[m - 1][n - 1]

"""Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
"""

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        pass

'''Set Matrix Zeroes

Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
'''

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        pass


"""Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

"""
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        pass