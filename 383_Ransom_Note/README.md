# 383. Ransom Note

## Problem Description

Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

Each letter in magazine can only be used once in ransomNote.

### Example 1:

**Input:** ransomNote = "a", magazine = "b"  
**Output:** false  

### Example 2:

**Input:** ransomNote = "aa", magazine = "ab"  
**Output:** false  

### Example 3:

**Input:** ransomNote = "aa", magazine = "aab"  
**Output:** true  

### Constraints:

- 1 <= ransomNote.length, magazine.length <= 10^5
- ransomNote and magazine consist of lowercase English letters.

# Intuition
To construct the ransom note, each character must be taken from the magazine **at most once**.
So the problem reduces to checking whether the magazine has **enough frequency** of every character
required by the ransom note.

# Approach
- Count the frequency of each character in `magazine`.
- Iterate through each character in `ransomNote`:
  - If the character is unavailable or its count is zero, return False.
  - Otherwise, decrement its count.
- If all characters are successfully matched, return True.

This avoids unnecessary complexity and works efficiently for large inputs.

# Complexity
- Time complexity: O(n), where n is the length of the magazine
- Space complexity: O(1), since we only store counts for 26 lowercase letters

# Code
class Solution:
    def canConstruct(self, ransomNote, magazine):
        count = [0] * 26
        
        for c in magazine:
            count[ord(c) - ord('a')] += 1
        
        for c in ransomNote:
            idx = ord(c) - ord('a')
            if count[idx] == 0:
                return False
            count[idx] -= 1
        
        return True