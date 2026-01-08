# 49. Group Anagrams

## Problem Description

Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

### Example 1:

**Input:** strs = ["eat","tea","tan","ate","nat","bat"]  
**Output:** [["bat"],["nat","tan"],["ate","eat","tea"]]  

### Example 2:

**Input:** strs = [""]  
**Output:** [[""]]  

### Example 3:

**Input:** strs = ["a"]  
**Output:** [["a"]]  

### Constraints:

- 1 <= strs.length <= 10^4
- 0 <= strs[i].length <= 100
- strs[i] consists of lowercase English letters.

# Intuition
Anagrams share the **same character frequencies**.
If two strings have identical character counts, they belong to the same group.
So the real task is finding a reliable **key** that represents each word’s character makeup.

# Approach
- For each string, build a frequency count of 26 lowercase letters.
- Convert this count into a tuple so it can be used as a dictionary key.
- Group strings that share the same frequency key.
- Return all grouped values.

This avoids sorting strings repeatedly and stays efficient.

# Complexity
- Time complexity: O(n × k), where n is the number of strings and k is the maximum string length
- Space complexity: O(n × k), for storing frequency keys and grouped strings

# Code
class Solution:
    def groupAnagrams(self, strs):
        groups = {}

        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            key = tuple(count)

            if key not in groups:
                groups[key] = []
            groups[key].append(s)

        return list(groups.values())