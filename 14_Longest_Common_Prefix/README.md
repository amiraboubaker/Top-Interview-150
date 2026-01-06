# 14. Longest Common Prefix

Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

Example 1:

Input: strs = ["flower","flow","flight"]

Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]

Output: ""

Explanation: There is no common prefix among the input strings.

Constraints:

1 <= strs.length <= 200

0 <= strs[i].length <= 200

strs[i] consists of only lowercase English letters if it is non-empty.

# Intuition

Find the minimum length string, then check each character position across all strings.

# Approach

1. If strs is empty, return ""

2. Find min_len = min(len(s) for s in strs)

3. For i in range(min_len):

   for s in strs:

       if s[i] != strs[0][i]:

           return strs[0][:i]

4. Return strs[0][:min_len]

# Complexity

- Time: O(m*n) where m is min length, n is number of strings

- Space: O(1)

# Code

```python
from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        min_len = min(len(s) for s in strs)
        for i in range(min_len):
            for s in strs:
                if s[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0][:min_len]
```