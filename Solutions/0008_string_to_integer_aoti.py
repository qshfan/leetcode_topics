# 0008_string_to_integer_aoti
# Medium
# Keys #math #strOps

import re


class Solution:
    def myAtoi(self, a_str: str) -> int:
        a_str = a_str.strip()
        a_str = re.findall(r"(^[\+\-0]*\d+)\D*", a_str)

        try:
            res = int("".join(a_str))
            MAX_INT = 2 ** 31 - 1
            MIN_INT = -(2 ** 31)
            if res > MAX_INT:
                return MAX_INT
            elif res < MIN_INT:
                return MIN_INT
            else:
                return res
        except:
            return 0