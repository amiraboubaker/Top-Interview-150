# 6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

P   A   H   N

A P L S I I G

Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);

Example 1:

Input: s = "PAYPALISHIRING", numRows = 3

Output: "PAHNAPLSIIGYIR"

Example 2:

Input: s = "PAYPALISHIRING", numRows = 4

Output: "PINALSIGYAHRPI"

Explanation:

P     I    N

A   L S  I G

Y A   H R

P     I

Example 3:

Input: s = "A", numRows = 1

Output: "A"

Constraints:

1 <= s.length <= 1000

s consists of English letters (lower-case and upper-case), ',' and '.'.

1 <= numRows <= 1000

# Intuition

Simulate the zigzag pattern by placing characters in rows, changing direction at top and bottom.

# Approach

1. If numRows == 1, return s

2. Create list of strings for rows

3. cur = 0, down = True

4. For each char in s:

   rows[cur] += char

   if down:

       if cur == numRows - 1:

           down = False

           cur -= 1

       else:

           cur += 1

   else:

       if cur == 0:

           down = True

           cur += 1

       else:

           cur -= 1

5. Join rows

# Complexity

- Time: O(n)

- Space: O(n)

# Code

```python
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        rows = ["" for _ in range(numRows)]
        cur = 0
        down = True
        for c in s:
            rows[cur] += c
            if down:
                if cur == numRows - 1:
                    down = False
                    cur -= 1
                else:
                    cur += 1
            else:
                if cur == 0:
                    down = True
                    cur += 1
                else:
                    cur -= 1
        return "".join(rows)
```