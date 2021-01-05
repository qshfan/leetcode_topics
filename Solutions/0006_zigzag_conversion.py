# 0006_zigzag_conversion
# Medium
# Keys: #pointer


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        step, index = 1, 0
        L = [""] * numRows

        for ch in s:
            L[index] += ch

            if index == 0:
                step = 1
            elif index == numRows - 1:
                step = -1

            index += step
        return "".join(L)
