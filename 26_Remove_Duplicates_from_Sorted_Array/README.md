# 26. Remove Duplicates from Sorted Array

Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

## Intuition
Since the array is sorted, duplicates are consecutive. To remove duplicates in-place, we only need to keep the first occurrence of each number and overwrite subsequent duplicates.

## Approach
Use a pointer k to track the position of the next unique element.
Traverse the array:
If the current number nums[i] is different from nums[k - 1] (the last unique number), place it at nums[k] and increment k.
At the end, k is the number of unique elements and the first k elements of nums are the unique numbers in order.

## Complexity
- Time complexity: O(n)
- Space complexity: O(1)

## Code
```python
class Solution:
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        k = 1
        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1
        return k
```

## Examples
- Input: nums = [1,1,2]  
  Output: 2, nums = [1,2,_]

- Input: nums = [0,0,1,1,1,2,2,3,3,4]  
  Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]