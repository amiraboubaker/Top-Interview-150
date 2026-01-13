3453. Separate Squares I
Solved
Medium
Topics
premium lock icon
Companies
Hint
You are given a 2D integer array squares. Each squares[i] = [xi, yi, li] represents the coordinates of the bottom-left point and the side length of a square parallel to the x-axis.

Find the minimum y-coordinate value of a horizontal line such that the total area of the squares above the line equals the total area of the squares below the line.

Answers within 10-5 of the actual answer will be accepted.

Note: Squares may overlap. Overlapping areas should be counted multiple times.

# Intuition

The area of all square parts lying below a horizontal line increases monotonically as the line moves upward. At the lowest possible height, the area below the line is zero, and at the highest possible height, it equals the total area of all squares. Therefore, there exists a height where the area below the line is exactly half of the total area, which can be found using binary search.

# Approach

1. Compute the total area of all squares and divide it by two to obtain the target area.
2. Determine the minimum and maximum possible y-values based on square boundaries.
3. Define a helper function that calculates the total area of square portions below a given height.
4. Perform a binary search on the y-axis:
   - If the area below the midpoint is smaller than the target, move the lower bound up.
   - Otherwise, move the upper bound down.
5. Repeat until the required precision is reached and return the smallest valid y-value.

# Complexity

- Time complexity:  
  Each binary search step computes the area in O(n), and the search runs for a constant number of iterations to achieve precision, resulting in O(n log P), where P is the precision.

- Space complexity:  
  Only constant extra space is used, so O(1).