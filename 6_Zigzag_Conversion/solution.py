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