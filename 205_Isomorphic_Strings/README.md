# 205. Isomorphic Strings

## Problem Description

Given two strings s and t, determine if they are isomorphic.

Two strings s and t are isomorphic if the characters in s can be replaced to get t.

All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

### Example 1:

**Input:** s = "egg", t = "add"  
**Output:** true  

### Example 2:

**Input:** s = "foo", t = "bar"  
**Output:** false  

### Example 3:

**Input:** s = "paper", t = "title"  
**Output:** true  

### Constraints:

- 1 <= s.length <= 5 * 10^4
- t.length == s.length
- s and t consist of any valid ascii character.

# Intuition
Two strings are isomorphic if there is a **one-to-one mapping** between characters of `s` and `t`.
Each character in `s` must always map to the same character in `t`, and no two characters in `s`
can map to the same character in `t`.

# Approach
- Use two hash maps:
  - One to map characters from `s` to `t`
  - Another to map characters from `t` to `s` (to prevent collisions)
- Traverse both strings simultaneously:
  - If a mapping already exists, ensure it is consistent
  - If not, create the mapping in both directions
- If any inconsistency appears, return False
- If the loop finishes successfully, return True

# Complexity
- Time complexity: O(n), where n is the length of the strings
- Space complexity: O(n), for the character mappings

# Code
class Solution:
    def isIsomorphic(self, s, t):
        map_st = {}
        map_ts = {}

        for c1, c2 in zip(s, t):
            if c1 in map_st and map_st[c1] != c2:
                return False
            if c2 in map_ts and map_ts[c2] != c1:
                return False
            map_st[c1] = c2
            map_ts[c2] = c1

        return True