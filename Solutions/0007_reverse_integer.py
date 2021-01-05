# 0007_reverse_integer
# Easy
# Keys: #math
# 123 -> 321


class Solution:
    # using string reverse
    def reverse(self, x: int) -> int:
        s = [1, -1][x < 0]
        r = int(str(abs(x))[::-1])
        return s * r * (r < 2 ** 31)

    # using math
    def reverse_2(self, x: int) -> int:
        d = abs(x)
        newNum = 0

        while d > 0:
            d, m = divmod(d, 10)
            newNum = (newNum * 10) + m

        if newNum >= (2 ** 31) - 1:
            return 0
        return newNum if x > 0 else newNum * -1
