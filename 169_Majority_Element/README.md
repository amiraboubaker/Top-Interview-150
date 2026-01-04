# 169. Majority Element

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n/2⌋ times. You may assume that the majority element always exists in the array.

## Intuition
The majority element appears more than n/2 times, so there can only be one such element. Instead of counting all elements, we can use a clever linear-time, constant-space approach called Boyer-Moore Voting Algorithm.

## Approach
Initialize candidate and count = 0.
Traverse the array:
If count == 0, set candidate = num.
If num == candidate, increment count.
Else, decrement count.
After one pass, candidate will be the majority element.

## Complexity
- Time complexity: O(n)
- Space complexity: O(1)

## Code
```python
class Solution:
    def majorityElement(self, nums):
        count = 0
        candidate = None
        
        for num in nums:
            if count == 0:
                candidate = num
            count += (1 if num == candidate else -1)
        
        return candidate
```

## Examples
- Input: nums = [3,2,3]  
  Output: 3

- Input: nums = [2,2,1,1,1,2,2]  
  Output: 2