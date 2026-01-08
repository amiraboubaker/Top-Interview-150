# 73. Set Matrix Zeroes

## Problem Description

Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

### Example 1:

**Input:** matrix = [[1,1,1],[1,0,1],[1,1,1]]  
**Output:** [[1,0,1],[0,0,0],[1,0,1]]  

### Example 2:

**Input:** matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]  
**Output:** [[0,0,0,0],[0,4,5,0],[0,3,1,0]]  

### Constraints:

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 200
- -2^31 <= matrix[i][j] <= 2^31 - 1

# Intuition
Whenever an element is 0, its **entire row and column** must become 0.  
To do this **in-place** without extra space, we can cleverly use the **first row and first column** as markers.

# Approach
1. Check if the **first row** and **first column** initially contain zeros (we'll need this later).  
2. Use the **first row** to mark which columns should be zeroed.  
3. Use the **first column** to mark which rows should be zeroed.  
4. Iterate over the matrix (excluding first row/column) to set zeros based on markers.  
5. Finally, set zeros for the first row/column if needed.

This avoids extra space and modifies the matrix in-place.

# Complexity
- Time complexity: O(m × n)  
- Space complexity: O(1) (in-place using first row/column as markers)

# Code
class Solution:
    def setZeroes(self, matrix):
        m, n = len(matrix), len(matrix[0])
        first_row_zero = any(matrix[0][j] == 0 for j in range(n))
        first_col_zero = any(matrix[i][0] == 0 for i in range(m))
        
        # Use first row/col as markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0
        
        # Set zeros based on markers
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
        
        # Zero first row/col if needed
        if first_row_zero:
            for j in range(n):
                matrix[0][j] = 0
        if first_col_zero:
            for i in range(m):
                matrix[i][0] = 0