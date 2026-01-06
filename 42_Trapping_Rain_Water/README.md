# 42. Trapping Rain Water

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]

Output: 6

Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:

Input: height = [4,2,0,3,2,5]

Output: 9

Constraints:

n == height.length

1 <= n <= 2 * 104

0 <= height[i] <= 105

# Intuition

For each bar, the trapped water is determined by the minimum of the maximum heights to its left and right minus its own height. We use two pointers to efficiently compute this.

# Approach

1. Use two pointers, left and right, starting from ends.

2. Track max_left and max_right.

3. Move the pointer with smaller max, add water.

# Complexity

- Time: O(n)

- Space: O(1)

# Code

```python
from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]
        water = 0
        while left < right:
            if max_left < max_right:
                left += 1
                max_left = max(max_left, height[left])
                water += max_left - height[left]
            else:
                right -= 1
                max_right = max(max_right, height[right])
                water += max_right - height[right]
        return water
```