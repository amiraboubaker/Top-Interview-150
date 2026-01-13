from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        """
        :type squares: List[List[int]]
        :rtype: float
        """
        total_area = 0
        min_y = float('inf')
        max_y = -float('inf')

        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)

        half = total_area / 2.0

        def area_below(h):
            area = 0.0
            for x, y, l in squares:
                if h <= y:
                    continue
                elif h >= y + l:
                    area += l * l
                else:
                    area += l * (h - y)
            return area

        left, right = min_y, max_y
        for _ in range(60):
            mid = (left + right) / 2.0
            if area_below(mid) < half:
                left = mid
            else:
                right = mid

        return left

# Test
if __name__ == "__main__":
    sol = Solution()
    # Example: one square at [0,0,2], total area 4, half 2, y should be 1 (middle)
    squares = [[0, 0, 2]]
    result = sol.separateSquares(squares)
    print(f"Result: {result}")  # Should be 1.0