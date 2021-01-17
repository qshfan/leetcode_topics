# 1641_count_sorted_vowel_strings
# Medium
# keys: #dp #prefix_sum
from itertools import accumulate


class Solution:
    def countVowelStrings(self, n: int) -> int:
        res = [1, 1, 1, 1, 1]
        i = 1
        while i < n:
            res = list(accumulate(res, initial=0))
            i += 1
        return sum(res)

    def countVowelStrings_2(self, n: int) -> int:
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = a + e + i + o + u, e + i + o + u, i + o + u, o + u, u

        return a + e + i + o + u
