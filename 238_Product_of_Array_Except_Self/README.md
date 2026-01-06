# 238. Product of Array Except Self

# Intuition
For each index, the desired value is the product of all elements except the one at that index. Since division is not allowed, we can split the product into two parts: the product of all elements to the left of the index and the product of all elements to the right. Multiplying these two gives the correct result for each position and naturally handles zeros without special cases.

# Approach
1. Initialize an output array `answer` with 1s.
2. Traverse the array from left to right, maintaining a running product of elements before the current index and store it in `answer[i]`.
3. Traverse the array from right to left, maintaining a running product of elements after the current index and multiply it into `answer[i]`.
4. Return the `answer` array.

# Complexity
- Time complexity: O(n) — two linear passes through the array.
- Space complexity: O(1) extra space, excluding the output array.

# Code
```python
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        answer = [1] * n

        left = 1
        for i in range(n):
            answer[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right
            right *= nums[i]

        return answer
```