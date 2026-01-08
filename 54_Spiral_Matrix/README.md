# 54. Spiral Matrix

## Problem Description

Given an m x n matrix, return all elements of the matrix in spiral order.

### Example 1:

**Input:** matrix = [[1,2,3],[4,5,6],[7,8,9]]  
**Output:** [1,2,3,6,9,8,7,4,5]  

### Example 2:

**Input:** matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]  
**Output:** [1,2,3,4,8,12,11,10,9,5,6,7]  

### Constraints:

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 10
- -100 <= matrix[i][j] <= 100

# Intuition
The spiral order traversal works by repeatedly removing the outer layer of the matrix.
Each iteration collects the top row, right column, bottom row, and left column, then moves inward
until all elements are processed.

# Approach
Continuously peel off the matrix layer by layer:

Take the first row from left to right.
Take the last element of each remaining row from top to bottom.
Take the last row from right to left.
Take the first element of each remaining row from bottom to top.
Repeat this process until the matrix is empty.

# Complexity
Time complexity: O(m × n)  
Space complexity: O(1) extra space (excluding the output list)

# Code
class Solution:
    def spiralOrder(self, matrix):
        res = []
        while matrix:
            res += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    res.append(row.pop())
            if matrix:
                res += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    res.append(row.pop(0))
        return res