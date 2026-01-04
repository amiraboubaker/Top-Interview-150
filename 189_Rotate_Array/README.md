# 189. Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.

## Intuition
Rotating an array to the right by k steps means moving the last k elements to the front. To do this in-place with O(1) extra space, we can use array reversal. First, reverse the entire array, then reverse the first k elements, and finally reverse the remaining elements.

## Approach
- Compute k = k % len(nums) to handle cases where k > n.
- Reverse the entire array.
- Reverse the first k elements.
- Reverse the elements from k to the end.
This achieves the rotation in-place.

## Complexity
- Time complexity: O(n), where n is the length of the array, as each element is reversed a constant number of times.
- Space complexity: O(1), using only a few extra variables.

## Code
```python
from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        self.reverse(nums, 0, n - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, n - 1)
    
    def reverse(self, nums: List[int], start: int, end: int) -> None:
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
```

## Examples
- Input: nums = [1,2,3,4,5,6,7], k = 3  
  Output: [5,6,7,1,2,3,4]

- Input: nums = [-1,-100,3,99], k = 2  
  Output: [3,99,-1,-100]

## Follow-up
This solution uses O(1) extra space by performing the rotation in-place through reversals.