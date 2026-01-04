# 27. Remove Element

Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.

## Intuition
We need to remove all instances of a specific value from the array in-place, keeping the relative order of the other elements. Using two pointers, we can overwrite the elements that are equal to val with the ones that are not.

## Approach
Initialize a pointer k at 0. Iterate through the array with index i. If nums[i] is not equal to val, set nums[k] to nums[i] and increment k. This effectively moves all non-val elements to the front of the array.

## Complexity
- Time complexity: O(n), where n is the length of the array, as we traverse it once.
- Space complexity: O(1), using only a constant amount of extra space.

## Code
```python
class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k
```

## Examples
- Input: nums = [3,2,2,3], val = 3  
  Output: 2, nums = [2,2,_,_]

- Input: nums = [0,1,2,2,3,0,4,2], val = 2  
  Output: 5, nums = [0,1,4,0,3,_,_,_]