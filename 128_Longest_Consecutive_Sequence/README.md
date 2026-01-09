# Intuition
We want the longest streak of consecutive numbers.
Sorting would work but is O(n log n), which is too slow.
Instead, we can use a set for O(1) lookups and only start counting sequences from numbers that are the beginning of a sequence.

# Approach
Put all numbers into a set num_set for O(1) lookup.
Iterate through each number num in num_set:
Only start counting if num - 1 is not in num_set (this ensures we start from the beginning of a sequence).
Count consecutive numbers by checking num + 1, num + 2, ... until the sequence breaks.
Track the maximum length found.
Return the maximum length.

# Complexity
Time complexity: O(n)
Each number is processed at most twice (once as a start, once when counted in a sequence).

Space complexity: O(n)
We store all numbers in a set.

# Code
```python
class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        max_len = 0

        for num in num_set:
            if num - 1 not in num_set:
                current = num
                length = 1
                while current + 1 in num_set:
                    current += 1
                    length += 1
                max_len = max(max_len, length)

        return max_len
```