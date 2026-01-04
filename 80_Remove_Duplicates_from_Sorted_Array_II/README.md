# 80. Remove Duplicates from Sorted Array II

Given an integer array nums sorted in non-decreasing order, remove some duplicates in-place such that each unique element appears at most twice. The relative order of the elements should be kept the same.

Since it is impossible to change the length of the array in some languages, you must instead have the result be placed in the first part of the array nums. More formally, if there are k elements after removing the duplicates, then the first k elements of nums should hold the final result. It does not matter what you leave beyond the first k elements.

Return k after placing the final result in the first k slots of nums.

Do not allocate extra space for another array. You must do this by modifying the input array in-place with O(1) extra memory.

## Intuition
Since the array is sorted, duplicates are adjacent. We need to allow each element to appear at most twice, so we can use a pointer to track where to place the next valid element, ensuring that for any position, the element isn't the same as the one two positions back.

## Approach
Use two pointers: i to track the position to place the next element, and j to iterate through the array. For each j, if i < 2 (allowing the first two elements) or nums[j] > nums[i-2] (meaning it's not a third duplicate), place nums[j] at nums[i] and increment i.

## Complexity
- Time complexity: O(n), where n is the length of the array, as we traverse it once.
- Space complexity: O(1), using only a few extra variables.

## Code
```python
class Solution:
    def removeDuplicates(self, nums):
        k = 0
        for num in nums:
            if k < 2 or num != nums[k - 2]:
                nums[k] = num
                k += 1
        return k
```

## Examples
- Input: nums = [1,1,1,2,2,3]  
  Output: 5, nums = [1,1,2,2,3,_]

- Input: nums = [0,0,1,1,1,1,2,3,3]  
  Output: 7, nums = [0,0,1,1,2,3,3,_,_]