from collections import deque

def simulateWaterFlow(heights, startRow, startCol):
    rows, cols = len(heights), len(heights[0])
    wetTime = [[-1 for _ in range(cols)] for _ in range(rows)]
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # Up, Down, Left, Right

    # BFS initialization
    queue = deque([(startRow, startCol)])
    wetTime[startRow][startCol] = 0  # Starting cell is wet at time 0

    while queue:
        row, col = queue.popleft()
        current_time = wetTime[row][col]

        # Explore neighbors
        for dr, dc in directions:
            newRow, newCol = row + dr, col + dc

            # Check bounds, height condition, and wetTime condition
            if (0 <= newRow < rows and 0 <= newCol < cols and
                heights[newRow][newCol] <= heights[row][col] and
                wetTime[newRow][newCol] == -1):
                
                # Update the time step and add to the queue
                wetTime[newRow][newCol] = current_time + 1
                queue.append((newRow, newCol))

    return wetTime