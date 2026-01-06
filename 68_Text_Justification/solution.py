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