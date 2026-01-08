# 202. Happy Number

## Problem Description

Write an algorithm to determine if a number n is happy.

A happy number is a number defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits.
Repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1.
Those numbers for which this process ends in 1 are happy.
Return true if n is a happy number, and false if not.

### Example 1:

**Input:** n = 19  
**Output:** true  

**Explanation:**  
1^2 + 9^2 = 1 + 81 = 82  
8^2 + 2^2 = 64 + 4 = 68  
6^2 + 8^2 = 36 + 64 = 100  
1^2 + 0^2 + 0^2 = 1 + 0 + 0 = 1  

### Example 2:

**Input:** n = 2  
**Output:** false  

### Constraints:

- 1 <= n <= 2^31 - 1

# Intuition
A number is happy if repeatedly replacing it with the **sum of the squares of its digits**
eventually leads to 1.  
If it doesn’t, it will fall into a **cycle** and loop forever.  
So the real problem is detecting a loop.

# Approach
- Repeatedly compute the sum of the squares of the digits of `n`.
- Keep a set of numbers already seen.
- If `n` becomes 1, return True.
- If `n` appears again, a cycle is detected → return False.

Simple cycle detection. Nothing mystical.

# Complexity
- Time complexity: O(log n) per iteration, with a small constant number of iterations
- Space complexity: O(log n), for storing seen numbers

# Code
class Solution:
    def isHappy(self, n):
        seen = set()

        while n != 1 and n not in seen:
            seen.add(n)
            n = sum(int(d) ** 2 for d in str(n))

        return n == 1