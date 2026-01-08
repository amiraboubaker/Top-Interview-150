# 289. Game of Life

## Problem Description

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state of the board is determined by applying the above rules simultaneously to every cell in the current state of the m x n grid board. In this process, births and deaths occur simultaneously.

Given the current state of the board, update the board to reflect its next state.

Note that you do not need to return anything.

### Example 1:

**Input:** board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]  
**Output:** [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]  

### Example 2:

**Input:** board = [[1,1],[1,0]]  
**Output:** [[1,1],[1,1]]  

### Constraints:

- m == board.length
- n == board[i].length
- 1 <= m, n <= 25
- board[i][j] is 0 or 1.

### Follow up:

Could you solve it in-place? Remember that the board needs to be updated simultaneously: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches upon the border of the array (i.e., live cells reach the border). How would you address these problems?

# Intuition
The Game of Life requires updating all cells simultaneously based on their current neighbors. To do this in-place, we need to mark changes without affecting neighbor counts for other cells.

# Approach
1. Iterate through each cell and count its live neighbors using the current state.
2. Based on the rules, mark cells that will change: use -1 for live cells that die, and 2 for dead cells that become live.
3. After processing all cells, update the board: -1 becomes 0, 2 becomes 1.

This ensures simultaneous updates.

# Complexity
- Time complexity: O(m × n) — each cell is visited once, and neighbor checks are constant time.
- Space complexity: O(1) — in-place modification.

# Code
class Solution:
    def gameOfLife(self, board):
        if not board or not board[0]:
            return
        m, n = len(board), len(board[0])
        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        for i in range(m):
            for j in range(n):
                live_neighbors = 0
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < m and 0 <= nj < n and abs(board[ni][nj]) == 1:
                        live_neighbors += 1
                if board[i][j] == 1:
                    if live_neighbors < 2 or live_neighbors > 3:
                        board[i][j] = -1  # live to dead
                else:
                    if live_neighbors == 3:
                        board[i][j] = 2  # dead to live
        for i in range(m):
            for j in range(n):
                if board[i][j] == -1:
                    board[i][j] = 0
                elif board[i][j] == 2:
                    board[i][j] = 1