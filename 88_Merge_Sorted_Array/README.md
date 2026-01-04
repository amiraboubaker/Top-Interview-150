# Intuition
Because nums1 has extra space at the end, merging from the back prevents overwriting elements that have not yet been compared. The largest elements should be placed first at the end of nums1.

# Approach
Use three pointers:
- i points to the last valid element in nums1
- j points to the last element in nums2
- k points to the last position in nums1

Compare nums1[i] and nums2[j], place the larger value at nums1[k], and move the pointers accordingly. Continue until all elements from nums2 are merged.

# Complexity
- Time complexity: O(m + n)
- Space complexity: O(1)

# Code
```python
class Solution:
    def merge(self, nums1, m, nums2, n):
        i = m - 1          # pointer for last valid element in nums1
        j = n - 1          # pointer for last element in nums2
        k = m + n - 1      # pointer for end of nums1

        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

```