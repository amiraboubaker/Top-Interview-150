# Intuition
The array should contain every number from 1 to n exactly once. Since one number is duplicated, another number must be missing. By tracking which numbers have already appeared, we can identify the duplicate. The missing number is the one from 1 to n that never appears.

# Approach
1. Create a boolean or set structure to record seen numbers.
2. Traverse the array:
   - If a number has already been seen, it is the duplicate.
   - Otherwise, mark it as seen.
3. After processing the array, iterate from 1 to n:
   - The number that was never seen is the missing number.
4. Return the duplicate and the missing number as an array.

# Complexity
1. Time Complexity: O(n), because the array and the range 1 to n are each scanned once.
2. Space Complexity: O(n), due to the extra structure used to track seen numbers.

# Code
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        seen = set()
        duplicate = -1

        for num in nums:
            if num in seen:
                duplicate = num
            else:
                seen.add(num)

        missing = -1
        for i in range(1, n + 1):
            if i not in seen:
                missing = i
                break

        return [duplicate, missing]