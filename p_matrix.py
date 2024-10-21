"""
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
"""
def isValidSudoku(board):
    # Initialize sets to track seen digits for each row, each column, and each 3x3 sub-box
    # We create a list of 9 sets for rows, 9 sets for columns, and 9 sets for sub-boxes.
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    # Iterate through each cell in the 9x9 board
    for i in range(9):  # Loop through each row (0 to 8)
        for j in range(9):  # Loop through each column (0 to 8)
            num = board[i][j]  # Get the value at position (i, j)
            
            # If the current cell is empty (contains '.'), skip to the next iteration
            if num == '.':
                continue  # Move to the next cell
            
            # Calculate the index for the 3x3 sub-box. This formula helps map (i, j)
            # into a single box index (0 to 8) corresponding to the 3x3 grid.
            box_index = (i // 3) * 3 + (j // 3)
            
            # Check if the number is already in the current row, column, or sub-box
            # If the number exists in any of the sets, return False since it's invalid
            if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                return False  # The board is invalid because the number is repeated
            
            # Add the number to the corresponding row set, column set, and sub-box set
            # This means the number is now "seen" for this row, column, and sub-box
            rows[i].add(num)  # Add number to the current row's set
            cols[j].add(num)  # Add number to the current column's set
            boxes[box_index].add(num)  # Add number to the current 3x3 sub-box's set
    
    # If no rule violations were found, return True, indicating the board is valid
    return True

"""
Given an m x n matrix, return all elements of the matrix in spiral order.
Input: matrix = 
[
[1,2,3],
[4,5,6],
[7,8,9]
]
Output: [1,2,3,6,9,8,7,4,5]

"""

def spiralOrder(matrix):
    # Initialize an empty list to store the spiral order result
    result = []
    
    # Define the boundaries of the matrix that we will use to control the spiral movement
    top, bottom = 0, len(matrix) - 1  # top and bottom rows
    left, right = 0, len(matrix[0]) - 1  # left and right columns
    
    # Loop until all boundaries are crossed
    while top <= bottom and left <= right:
        
        # Step 1: Traverse from left to right along the top row
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1  # After traversing the top row, move the top boundary down by 1
        
        # Step 2: Traverse from top to bottom along the rightmost column
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1  # After traversing the rightmost column, move the right boundary left by 1
        
        # Step 3: Traverse from right to left along the bottom row (if still within bounds)
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1  # After traversing the bottom row, move the bottom boundary up by 1
        
        # Step 4: Traverse from bottom to top along the leftmost column (if still within bounds)
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1  # After traversing the leftmost column, move the left boundary right by 1
    
    # Return the list of elements in spiral order
    return result


"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. 
DO NOT allocate another 2D matrix and do the rotation.

"""

def rotate(matrix):
    n = len(matrix)  # Get the size of the matrix (n x n)
    
    # Step 1: Transpose the matrix (swap matrix[i][j] with matrix[j][i])
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    # Step 2: Reverse each row
    for i in range(n):
        matrix[i].reverse()  # Reverse the current row

"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
"""

def setZeroes(matrix):
    m, n = len(matrix), len(matrix[0])  # Get dimensions of the matrix
    first_row_has_zero = False  # Flag for the first row
    first_col_has_zero = False  # Flag for the first column
    
    # Step 1: Determine which rows and columns need to be set to 0
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                # Mark the corresponding first row and first column
                matrix[0][j] = 0  # Mark the first row for column j
                matrix[i][0] = 0  # Mark the first column for row i
                # If it's in the first row or first column, set the respective flags
                if i == 0:
                    first_row_has_zero = True
                if j == 0:
                    first_col_has_zero = True
    
    # Step 2: Use markers in the first row and first column to set zeros
    for i in range(1, m):  # Skip the first row
        for j in range(1, n):  # Skip the first column
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0  # Set matrix[i][j] to 0 if it's marked
    
    # Step 3: Zero out the first row if needed
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0  # Set the entire first row to 0
    
    # Step 4: Zero out the first column if needed
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0  # Set the entire first column to 0


"""
According to Wikipedia's article: 
"The Game of Life, also known simply as Life, 
is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: 
live (represented by a 1) or dead (represented by a 0). 
Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using 
the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, 
where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

"""


def gameOfLife(board):
    m, n = len(board), len(board[0])  # Dimensions of the board

    # Helper function to count live neighbors around the cell (i, j)
    def count_live_neighbors(i, j):
        directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
        live_neighbors = 0
        for direction in directions:
            ni, nj = i + direction[0], j + direction[1]
            if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                live_neighbors += 1
        return live_neighbors
    
    # Step 1: Determine the next state for each cell using the current board
    for i in range(m):
        for j in range(n):
            live_neighbors = count_live_neighbors(i, j)
            
            # Apply the Game of Life rules
            if board[i][j] == 1:  # Live cell
                if live_neighbors < 2 or live_neighbors > 3:
                    board[i][j] = 2  # Mark live cell to die (1 -> 0)
            else:  # Dead cell
                if live_neighbors == 3:
                    board[i][j] = -1  # Mark dead cell to become live (0 -> 1)
    
    # Step 2: Update the board to the final state (from encoded states)
    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0  # Live cell that became dead
            elif board[i][j] == -1:
                board[i][j] = 1  # Dead cell that became live



def game_of_life(board):
    m, n = len(board), len(board[0])

    # Iterate through each cell in the board
    for i in range(m):
        for j in range(n):
            neighbors = 0

            # Count the number of live neighbors for the current cell
            # We use a double loop to check the 8 neighboring cells
            # (the 3x3 grid centered on the current cell)
            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    # Skip the current cell itself (dx, dy) == (0, 0)
                    if dx == dy == 0:
                        continue
                    
                    # Calculate the coordinates of the neighboring cell
                    x, y = i + dx, j + dy
                    
                    # Check if the neighboring cell is within the board bounds
                    # and if it's currently in a "live" state (1 or 2)
                    if 0 <= x < m and 0 <= y < n and board[x][y] in [1, 2]:
                        neighbors += 1

            # Apply the rules of the Game of Life
            if board[i][j] == 1:  # Live cell
                # Rule 1: Any live cell with fewer than two live neighbors dies,
                # as if caused by under-population.
                # Rule 3: Any live cell with more than three live neighbors dies,
                # as if by over-population.
                if neighbors < 2 or neighbors > 3:
                    board[i][j] = 2  # Cell will die in the next generation
            else:  # Dead cell
                # Rule 4: Any dead cell with exactly three live neighbors
                # becomes a live cell, as if by reproduction.
                if neighbors == 3:
                    board[i][j] = 3  # Cell will become alive in the next generation

    # Update the board in-place
    for i in range(m):
        for j in range(n):
            if board[i][j] == 2:
                board[i][j] = 0  # Dead
            elif board[i][j] == 3:
                board[i][j] = 1  # Alive

    return board