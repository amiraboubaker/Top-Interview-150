# Intuition
We need to check if any number appears at least twice in the array and the indices of these duplicates are at most `k` apart.  
A simple approach is to remember the last index of each number as we scan through the array.

# Approach
1. Create a dictionary `last_index` to store the last seen index of each number.
2. Iterate through the array with index `i` and value `num`:
   - If `num` is already in `last_index` and the difference between current index `i` and the stored index is ≤ `k`, return `True`.
   - Otherwise, update `last_index[num]` to `i`.
3. If the loop finishes without finding any duplicates within distance `k`, return `False`.

# Complexity
- Time complexity: O(n)  
  Scanning the array takes O(n). Dictionary lookups and updates are O(1) on average.  

- Space complexity: O(n)  
  We store at most one index per unique number.

# Code
```python
class Solution:
    def containsNearbyDuplicate(self, nums, k):
        last_index = {}

        for i, num in enumerate(nums):
            if num in last_index and i - last_index[num] <= k:
                return True
            last_index[num] = i

        return False
```