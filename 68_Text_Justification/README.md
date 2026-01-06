# 68. Text Justification

Given an array of strings words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line does not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left-justified, and no extra space is inserted between words.

Note:

A word is defined as a character sequence consisting of non-space characters only.

Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.

The input array words contains at least one word.

Example 1:

Input: words = ["This", "is", "an", "example", "of", "text", "justification."], maxWidth = 16

Output:

[

   "This    is    an",

   "example  of text",

   "justification.  "

]

Example 2:

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16

Output:

[

  "What   must   be",

  "acknowledgment  ",

  "shall be        "

]

Explanation: Note that the last line is "shall be    " instead of "shall     be", because the last line must be left-justified instead of fully-justified.

Note that the second line is also left-justified because it contains only one word.

Example 3:

Input: words = ["Science","is","what","we","understand","well","enough","to","explain","to","a","computer.","Art","is","everything","else","we","do"], maxWidth = 20

Output:

[

  "Science  is  what we",

  "understand      well",

  "enough to explain to",

  "a  computer.  Art is",

  "everything  else  we",

  "do                  "

]

Constraints:

1 <= words.length <= 300

1 <= words[i].length <= 20

words[i] consists of only English letters and symbols.

1 <= maxWidth <= 100

words[i].length <= maxWidth

# Intuition

Group words into lines greedily, then justify each line: distribute spaces evenly for full lines, left justify for last line.

# Approach

1. Initialize result list.

2. Use i to track current word.

3. While i < len(words):

   Collect words for a line until adding next would exceed maxWidth.

   If last line or single word, left justify.

   Else, calculate spaces per gap, distribute extra to left gaps.

4. Build the string for each line.

# Complexity

- Time: O(n) where n is total characters

- Space: O(m) for result

# Code

```python
from typing import List

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        i = 0
        while i < len(words):
            line = []
            line_len = 0
            while i < len(words) and line_len + len(words[i]) + len(line) <= maxWidth:
                line.append(words[i])
                line_len += len(words[i])
                i += 1
            if i == len(words) or len(line) == 1:
                s = ' '.join(line)
                s += ' ' * (maxWidth - len(s))
                result.append(s)
            else:
                total_spaces = maxWidth - line_len
                gaps = len(line) - 1
                space_per_gap = total_spaces // gaps
                extra = total_spaces % gaps
                s = line[0]
                for j in range(1, len(line)):
                    spaces = space_per_gap + (1 if j <= extra else 0)
                    s += ' ' * spaces + line[j]
                result.append(s)
        return result
```